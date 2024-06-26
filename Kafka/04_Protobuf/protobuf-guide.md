# Protobuf

Google Protocol Buffers, commonly known as Protobuf, is a language- and platform-neutral way of serializing structured data. It is useful for developing programs to communicate with each other over a network or for storing data. Protobuf is similar to XML or JSON but is smaller, faster, and simpler.

Reference:

[Cloudflare’s Trillion-Message Kafka Infrastructure: A Deep Dive](https://blog.bytebytego.com/p/cloudflares-trillion-message-kafka)

## Documentation:

[Official Documentation](https://protobuf.dev/)

[Language Guide (proto 3)](https://protobuf.dev/programming-guides/proto3/)

[Protocol Buffer Basics: Python](https://protobuf.dev/getting-started/pythontutorial/)

## Key Concept
### 1. Schema Defination 
Protobuf use a `.proto` file to define the structure the date. This file specify the data types and structure of the data to be serialized

### 2. Serialization and Deserialization
#### Serialization:
Serialization is the process of converting an object or data structure into a format that can be easily saved to a file, a database, or transmitted over a network. The serialized format is often a byte stream or a string format like JSON or XML.
```py
    import json

    data = {'name': 'Alice', 'age': 30, 'city': 'New York'}
    json_string = json.dumps(data)
    print(json_string)
```
#### Deserialization:
Deserialization is the process of converting the serialized format back into an object or data structure that can be used within the program. It is essentially the reverse of serialization.
```py
    import json

    json_string = '{"name": "Alice", "age": 30, "city": "New York"}'
    data = json.loads(json_string)
    print(data)
```

### 3. Generated Code
Protobuf generates code from the `.proto`file for the specified language like python, c++, java. The generated code includes the serialization and deserialization functions for the specified data structure. 

### Example
Let's go with python

### Step 1: Define the Schema

Create a file named `person.proto` with the following content:

```proto
syntax = "proto3";

message Person {
  string name = 1;
  int32 id = 2;
  string email = 3;
}
```

This defines a `Person` message with three fields: `name`, `id`, and `email`.

### Step 2: Generate Python Code

Use the `protoc` compiler to generate Python code from the `.proto` file.

```sh
protoc --python_out=. person.proto
```

This command generates a `person_pb2.py` file in the current directory.

### Step 3: Use the Generated Code in Python

```python
import person_pb2

# Create a new Person message
person = person_pb2.Person()
person.name = "John Doe"
person.id = 1234
person.email = "johndoe@example.com"

# Serialize the message to a byte string
serialized_person = person.SerializeToString()
print(f"Serialized data: {serialized_person}")

# Deserialize the byte string back into a Person message
new_person = person_pb2.Person()
new_person.ParseFromString(serialized_person)
print(f"Deserialized data: {new_person}")
print(f"Name: {new_person.name}, ID: {new_person.id}, Email: {new_person.email}")
```

### Explanation

1. **Import the Generated Code**

   ```python
   import person_pb2
   ```

   This imports the generated Python code for the `Person` message.

2. **Create a New Person Message**

   ```python
   person = person_pb2.Person()
   person.name = "John Doe"
   person.id = 1234
   person.email = "johndoe@example.com"
   ```

   This creates a new `Person` message and sets its fields.

3. **Serialize the Message**

   ```python
   serialized_person = person.SerializeToString()
   print(f"Serialized data: {serialized_person}")
   ```

   This serializes the `Person` message to a byte string.

4. **Deserialize the Byte String**

   ```python
   new_person = person_pb2.Person()
   new_person.ParseFromString(serialized_person)
   print(f"Deserialized data: {new_person}")
   print(f"Name: {new_person.name}, ID: {new_person.id}, Email: {new_person.email}")
   ```

   This deserializes the byte string back into a `Person` message and prints the field values.

### Advantages of Protobuf

1. **Compact and Efficient**: Protobuf is more efficient than XML and JSON in terms of both size and speed.
2. **Strongly Typed**: The generated code is strongly typed, which helps catch errors at compile-time rather than runtime.
3. **Backward and Forward Compatibility**: Protobuf supports adding new fields and deprecating old fields without breaking existing code.

### Conclusion

Google Protocol Buffers provide a powerful way to serialize structured data with high efficiency and ease of use. By defining your data schema in a `.proto` file and generating code for your desired language, you can easily serialize and deserialize data in a type-safe and efficient manner.