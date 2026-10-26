"""
Streamlit frontend for the Task Manager API.
Run with: streamlit run streamlit_app.py
Make sure the FastAPI backend is running at http://127.0.0.1:8000
"""

import streamlit as st
import requests

API_BASE = "http://127.0.0.1:8000/api/v1/tasks"

# ─────────────────────────── helpers ────────────────────────────


def fetch_tasks() -> list[dict]:
    try:
        r = requests.get(f"{API_BASE}/", timeout=5)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.ConnectionError:
        st.error("❌ Cannot connect to the FastAPI backend. Is it running?")
        return []


def create_task(title: str, description: str) -> dict | None:
    r = requests.post(
        f"{API_BASE}/",
        json={"task": title, "description": description},
        timeout=5,
    )
    if r.ok:
        return r.json()
    st.error(f"Create failed: {r.text}")
    return None


def toggle_task(task: dict) -> None:
    requests.patch(
        f"{API_BASE}/{task['id']}",
        json={"completed": not task["completed"]},
        timeout=5,
    )


def delete_task(task_id: int) -> None:
    requests.delete(f"{API_BASE}/{task_id}", timeout=5)


# ─────────────────────────── page config ────────────────────────

st.set_page_config(page_title="Task Manager", page_icon="✅", layout="centered")

st.title("✅ Task Manager")
st.caption("A simple to-do app powered by FastAPI + SQLite")

# ─────────────────────────── add task form ──────────────────────

with st.expander("➕ Add a new task", expanded=True):
    with st.form("add_task_form", clear_on_submit=True):
        title = st.text_input("Title", placeholder="e.g. Buy groceries")
        description = st.text_area("Description (optional)", placeholder="Details…", height=80)
        submitted = st.form_submit_button("Create Task", type="primary")
        if submitted:
            if not title.strip():
                st.warning("Title cannot be empty.")
            else:
                result = create_task(title.strip(), description.strip())
                if result:
                    st.success(f"Task **{result['title']}** created!")
                    st.rerun()

# ─────────────────────────── task list ──────────────────────────

st.divider()
tasks = fetch_tasks()

if not tasks:
    st.info("No tasks yet. Add one above!")
else:
    pending = [t for t in tasks if not t["completed"]]
    done = [t for t in tasks if t["completed"]]

    # ── Pending ──
    if pending:
        st.subheader(f"🔲 Pending ({len(pending)})")
        for task in pending:
            col1, col2, col3 = st.columns([0.6, 0.2, 0.2])
            with col1:
                st.markdown(f"**{task['title']}**")
                if task["description"]:
                    st.caption(task["description"])
            with col2:
                if st.button("✔ Done", key=f"done_{task['id']}"):
                    toggle_task(task)
                    st.rerun()
            with col3:
                if st.button("🗑 Delete", key=f"del_{task['id']}"):
                    delete_task(task["id"])
                    st.rerun()

    # ── Completed ──
    if done:
        st.subheader(f"✅ Completed ({len(done)})")
        for task in done:
            col1, col2, col3 = st.columns([0.6, 0.2, 0.2])
            with col1:
                st.markdown(f"~~{task['title']}~~")
                if task["description"]:
                    st.caption(task["description"])
            with col2:
                if st.button("↩ Undo", key=f"undo_{task['id']}"):
                    toggle_task(task)
                    st.rerun()
            with col3:
                if st.button("🗑 Delete", key=f"del_{task['id']}"):
                    delete_task(task["id"])
                    st.rerun()

# ─────────────────────────── stats ──────────────────────────────

if tasks:
    st.divider()
    total = len(tasks)
    completed = len([t for t in tasks if t["completed"]])
    col1, col2, col3 = st.columns(3)
    col1.metric("Total", total)
    col2.metric("Completed", completed)
    col3.metric("Pending", total - completed)
