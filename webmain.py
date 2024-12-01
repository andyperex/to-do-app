import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["n_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    print(todo)



st.title("My to do app")
st.subheader("Joyce come mocos")
st.write("Ela gosta de comer mocos com arros")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()



st.text_input(label="Lista de tareas",placeholder="Write something",
              on_change=add_todo, key="n_todo")

