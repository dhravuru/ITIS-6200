


sec_levels = {
    "U": 0,
    "C": 1,
    "S": 2,
    "TS": 3
}


class Subject:
    def __init__(self, name, max_level, current_level):
        if sec_levels[current_level] > sec_levels[max_level]:
            raise ValueError("Start level cannot be higher than max level")
        self.name = name
        self.max_level = max_level
        self.current_level = current_level

    def set_level(self, new_level):
        if sec_levels[new_level] > sec_levels[self.max_level]:
            print(f"[DENIED] {self.name} cannot exceed max level {self.max_level} ")
            return
        if sec_levels[new_level] < sec_levels[self.current_level]:
            print(f"[DENIED] {self.name} cannot lower level below current level {self.current_level}")
            return
        print(f"[LEVEL CHANGE] {self.name}: {self.current_level} -> {new_level}")
        self.current_level = new_level


class Object:
    def __init__(self, name, level):
        self.name = name
        self.level = level


class BLPSystem:
    def __init__(self):
        self.subjects = {}
        self.objects = {}

    def add_subject(self, name, max_level, start_level):
        self.subjects[name] = Subject(name, max_level, start_level)

    def add_object(self, name, level):
        self.objects[name] = Object(name, level)

    def read(self, subject_name, object_name):
        subject = self.subjects[subject_name]
        obj = self.objects[object_name]

        print(f"> Action: {subject.name.lower()} READ {obj.name}...")

        if sec_levels[obj.level] > sec_levels[subject.current_level]:
            if sec_levels[obj.level] <= sec_levels[subject.max_level]:
                print(f"> ALLOW: Obj Lvl {obj.level} <= Subj Max ({subject.max_level})")
                print(f"> INFO: Raising {subject.name.lower()}'s current level to {obj.level}.")
                subject.current_level = obj.level
                #print("[ALLOWED]")
            else:
                #print("[DENIED] No read up")
                print(f"> DENY: Obj Lvl ({obj.level}) > Subj Max ({subject.max_level}).")
        else: 
            #print("[ALLOWED]")
            print(f"> ALLOW: Obj Lvl {obj.level} <= Subj Curr ({subject.current_level}).")
        
        self.print_state()

    def write(self, subject_name, object_name):
        subject = self.subjects[subject_name]
        obj = self.objects[object_name]

        print(f"> Action: {subject.name.lower()} WRITE {obj.name}...")

        if sec_levels[subject.current_level] > sec_levels[obj.level]:
            print(f"> DENY: Subj Curr ({subject.current_level}) > Obj Lvl ({obj.level}) [No write down].")
        else:
            print(f"> ALLOW: Subj Curr ({subject.current_level}) <= Obj Lvl ({obj.level}).")
        
        self.print_state()

    def print_state(self):
        print("\n--- Current BLP State ---")
        for s in self.subjects.values():
            print(f"[Subject] {s.name.lower()}: Curr={s.current_level}, Max={s.max_level}")
        for o in self.objects.values():
            print(f"[Object] {o.name}: Lvl={o.level}")

        print("----------------------------\n")