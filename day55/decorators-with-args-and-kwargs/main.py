class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


# this decorator receives the create_blog_post() function which also receives a user argument. In this case, to access
# the user argument we use the first position for the auxiliary *args argument (aka. args[0]). Once we get it, we tap
# into its property called is_logged_in. If it is set to True then we execute the create_blog_post() function passing to
# it the same args[0] argument.
def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
        # else:
        #     print(f"Error: can't create blog post for user {args[0].name}. User not authenticated.")

    return wrapper


@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")


new_user = User("Felipe")
new_user.is_logged_in = True
# the create_blog_post() function only gets executed if we previously set the is_logged_in property to True
create_blog_post(new_user)
