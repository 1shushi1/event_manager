import bcrypt


def get_hashed_password(plain_text_password):
    """
    Return hashed password
    :param plain_text_password:
    :return:
    """
    return bcrypt.hashpw(plain_text_password, bcrypt.gensalt())

def check_password(plain_text_password, hashed_password):
    """
    Check hashed password. Using bcrypt, the salt is saved into the hash itself
    :param plain_text_password:
    :param hashed_password:
    :return:
    """
    return bcrypt.checkpw(plain_text_password, hashed_password)