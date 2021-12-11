DATABASES = {
    'default': {
        'ENGINE': 'loan',
        'CLIENT': {
            'host': 'mongodb+srv://loan:loan123456@cluster0.cqrpj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority',
            'username': 'loan',
            'password': 'loan123456',
            'authMechanism': 'SCRAM-SHA-1'
        }
    }
}