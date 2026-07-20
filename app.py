import streamlit as st

st.set_page_config(
    page_title="Python Tuple Visualizer",
    page_icon="📦",
    layout="wide"
)

st.title("📦 Python Tuple  Visualizer")

st.markdown("""
Learn Python **Tuple** interactively.

A **Tuple** is:
- ✅ Ordered
- ✅ Immutable (Cannot be changed)
- ✅ Allows duplicate values
- ✅ Can contain different data types
""")

# Sidebar Input
st.sidebar.header("Create a Tuple")

user_input = st.sidebar.text_input(
    "Enter elements separated by commas",
    "10,20,30,40,50"
)

elements = [x.strip() for x in user_input.split(",") if x.strip()]
my_tuple = tuple(elements)

st.subheader("Current Tuple")
st.code(str(my_tuple))
st.write("Length:", len(my_tuple))

# Visualization
st.subheader("Tuple Visualization")

if len(my_tuple) > 0:
    cols = st.columns(len(my_tuple))
    for i, value in enumerate(my_tuple):
        cols[i].metric(f"Index {i}", value)

# Operations
operation = st.selectbox(
    "Choose Tuple Operation",
    [
        "Length",
        "Access Element",
        "Slicing",
        "Count",
        "Index",
        "Concatenation",
        "Repetition",
        "Membership",
        "Iteration",
        "Min and Max",
        "Sorting",
        "Convert to List",
        "Nested Tuple"
    ]
)

st.divider()

if operation == "Length":
    st.success(f"Length = {len(my_tuple)}")

elif operation == "Access Element":
    if len(my_tuple) > 0:
        idx = st.number_input(
            "Enter Index",
            min_value=0,
            max_value=len(my_tuple) - 1,
            value=0
        )
        st.info(f"Element = {my_tuple[idx]}")
    else:
        st.warning("Tuple is empty.")

elif operation == "Slicing":
    start = st.number_input("Start", value=0)
    end = st.number_input("End", value=len(my_tuple))
    st.code(str(my_tuple[int(start):int(end)]))

elif operation == "Count":
    value = st.text_input("Value")
    if st.button("Count"):
        st.success(my_tuple.count(value))

elif operation == "Index":
    value = st.text_input("Value")
    if st.button("Find Index"):
        try:
            st.success(my_tuple.index(value))
        except ValueError:
            st.error("Value not found.")

elif operation == "Concatenation":
    new = st.text_input("Second Tuple", "60,70,80")
    second = tuple(x.strip() for x in new.split(",") if x.strip())
    st.write("Second Tuple")
    st.code(str(second))
    st.write("Result")
    st.code(str(my_tuple + second))

elif operation == "Repetition":
    n = st.slider("Times", 1, 10, 2)
    st.code(str(my_tuple * n))

elif operation == "Membership":
    value = st.text_input("Element")
    if value in my_tuple:
        st.success(f"{value} exists in the tuple.")
    else:
        st.error(f"{value} not found.")

elif operation == "Iteration":
    st.write("Traversing Tuple")
    for i, value in enumerate(my_tuple):
        st.write(f"Index {i} ➜ {value}")

elif operation == "Min and Max":
    try:
        nums = tuple(map(float, my_tuple))
        st.success(f"Minimum = {min(nums)}")
        st.success(f"Maximum = {max(nums)}")
    except ValueError:
        st.error("Works only with numeric tuples.")

elif operation == "Sorting":
    try:
        nums = tuple(map(float, my_tuple))
        st.code(str(tuple(sorted(nums))))
    except ValueError:
        st.code(str(tuple(sorted(my_tuple))))

elif operation == "Convert to List":
    st.code(str(list(my_tuple)))

elif operation == "Nested Tuple":
    nested = (
        my_tuple,
        ("A", "B", "C"),
        (100, 200)
    )
    st.code(str(nested))
    st.write("Access nested element:")
    st.success(nested[1][1])

st.divider()

st.subheader("Tuple Properties")

st.table({
    "Property": [
        "Ordered",
        "Mutable",
        "Duplicates",
        "Indexing",
        "Slicing",
        "Hashable"
    ],
    "Value": [
        "Yes",
        "No",
        "Yes",
        "Yes",
        "Yes",
        "Yes (if immutable elements)"
    ]
})

st.divider()

st.subheader("Built-in Tuple Methods")

st.code("""
tuple.count(x)
tuple.index(x)
len(tuple)
min(tuple)
max(tuple)
sorted(tuple)
tuple + tuple
tuple * n
""")

st.divider()

st.subheader("Quick Quiz")

question = st.radio(
    "Which statement is TRUE?",
    [
        "Tuple is mutable",
        "Tuple uses [] brackets",
        "Tuple is immutable",
        "Tuple cannot store duplicates"
    ]
)

if st.button("Check Answer"):
    if question == "Tuple is immutable":
        st.success("✅ Correct!")
    else:
        st.error("❌ Incorrect.")

st.divider()
st.caption("Python Tuple Interactive Visualizer using Streamlit")

