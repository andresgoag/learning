class ClassTest:
    # Instance method: gets the instance as the first argument.
    # The most common ones, are used to operate or modify the fields of the object.
    def instance_method(self):
        print(f"Called instance_method of {self}")

    # Class methods: Gets a class as the first argument.
    # Are used as a factory
    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

    # Static methods: gets nothing as the first argument.
    # It is used when a function by order should be inside a class
    @staticmethod
    def static_method():
        print("Called static_method.")



test = ClassTest()
test.instance_method() # An instance methods, needs an instance to be called.
ClassTest.class_method()  # Call a class method
ClassTest.static_method() # Has no information about the class.