class school:
    school_name = "adcet"
    print(school_name)
    @classmethod
    def change_name(cls,new_name):
        cls.school_name = new_name

school.change_name("adcet1")
print(school.school_name)