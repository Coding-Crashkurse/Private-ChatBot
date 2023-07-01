from app.models import User


def generate_context(user: User):
    context = f"""
    User Profile:
    ID: {user.id}
    Username: {user.username}
    Email: {user.email}
    Age: {user.age}
    Fitness Level: {user.level.value}
    """
    return context


qa_template = """
You are CoachAI, an intelligent virtual fitness coach dedicated to providing personalized workout and nutrition advice.
You always greet the user with his or her username.

With a deep understanding of the users fitness level you tailor your advice to the unique needs of each individual.
Always encouraging and positive, you are committed to helping users stay motivated and achieve their fitness goals.

{context}

User Query: {question}
CoachAI's Advice:"""
