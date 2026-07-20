import streamlit as st
import ast

st.set_page_config(page_title="Python Dictionary Visualizer", page_icon="📘", layout="wide")

st.title("📘 Python Dictionary Data Type Visualizer")

st.markdown("""
A **Dictionary** is:
- ✅ Ordered (Python 3.7+)
- ✅ Mutable
- ✅ Stores data as Key : Value pairs
- ✅ Keys are unique
- ✅ Values can be duplicated
""")

st.sidebar.header("Create a Dictionary")

default_dict = "{'Name':'Alice','Age':25,'City':'Chennai'}"

user_input = st.sidebar.text_area("Enter a Python Dictionary", default_dict)

try:
    my_dict = ast.literal_eval(user_input)
    if not isinstance(my_dict, dict):
        st.error("Please enter a valid dictionary.")
        st.stop()
except:
    st.error("Invalid dictionary format.")
    st.stop()

st.subheader("Current Dictionary")
st.code(str(my_dict))

st.subheader("Dictionary Visualization")

cols = st.columns(2)
cols[0].write("### Keys")
for k in my_dict.keys():
    cols[0].success(k)

cols[1].write("### Values")
for v in my_dict.values():
    cols[1].info(v)

operation = st.selectbox(
    "Choose Dictionary Operation",
    [
        "Length",
        "Access Value",
        "Add / Update",
        "Remove Key",
        "Keys",
        "Values",
        "Items",
        "Membership",
        "Iteration",
        "Copy",
        "Clear",
        "Nested Dictionary",
        "Dictionary Comprehension"
    ]
)

st.divider()

if operation == "Length":
    st.success(f"Length = {len(my_dict)}")

elif operation == "Access Value":
    key = st.text_input("Enter Key")
    if st.button("Get Value"):
        if key in my_dict:
            st.success(my_dict[key])
        else:
            st.error("Key not found.")

elif operation == "Add / Update":
    key = st.text_input("Key")
    value = st.text_input("Value")
    if st.button("Add / Update"):
        new_dict = my_dict.copy()
        new_dict[key] = value
        st.code(str(new_dict))

elif operation == "Remove Key":
    key = st.text_input("Key to Remove")
    if st.button("Remove"):
        new_dict = my_dict.copy()
        if key in new_dict:
            new_dict.pop(key)
            st.code(str(new_dict))
        else:
            st.error("Key not found.")

elif operation == "Keys":
    st.code(str(list(my_dict.keys())))

elif operation == "Values":
    st.code(str(list(my_dict.values())))

elif operation == "Items":
    st.code(str(list(my_dict.items())))

elif operation == "Membership":
    key = st.text_input("Enter Key")
    if key in my_dict:
        st.success(f"{key} exists.")
    else:
        st.error(f"{key} not found.")

elif operation == "Iteration":
    for k, v in my_dict.items():
        st.write(f"{k} ➜ {v}")

elif operation == "Copy":
    st.code(str(my_dict.copy()))

elif operation == "Clear":
    st.code(str(my_dict.copy().clear()))

elif operation == "Nested Dictionary":
    nested = {
        "Student": my_dict,
        "Marks": {"Math": 90, "Science": 95}
    }
    st.code(str(nested))
    st.success(nested["Marks"]["Science"])

elif operation == "Dictionary Comprehension":
    comp = {x: x*x for x in range(1, 6)}
    st.code(str(comp))

st.divider()

st.subheader("Dictionary Properties")

st.table({
    "Property": [
        "Ordered",
        "Mutable",
        "Duplicate Keys",
        "Duplicate Values",
        "Indexed",
        "Key-Value Pair"
    ],
    "Value": [
        "Yes",
        "Yes",
        "No",
        "Yes",
        "Access using Keys",
        "Yes"
    ]
})

st.divider()

st.subheader("Common Dictionary Methods")

st.code("""
dict.get(key)
dict.keys()
dict.values()
dict.items()
dict.update()
dict.pop(key)
dict.popitem()
dict.clear()
dict.copy()
dict.setdefault()
dict.fromkeys()
""")

st.divider()

st.subheader("Quick Quiz")

question = st.radio(
    "Which statement is TRUE?",
    [
        "Dictionary keys can be duplicated",
        "Dictionary is immutable",
        "Dictionary stores key-value pairs",
        "Dictionary uses () brackets"
    ]
)

if st.button("Check Answer"):
    if question == "Dictionary stores key-value pairs":
        st.success("✅ Correct!")
    else:
        st.error("❌ Incorrect.")

st.divider()
st.caption("Python Dictionary Interactive Visualizer using Streamlit")
