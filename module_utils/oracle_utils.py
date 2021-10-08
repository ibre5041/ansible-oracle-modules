
from ansible.module_utils.basic import *

def oracle_connect(module):
    """
    Connect to the database using parameter provided by Ansible module instance.
    Return: connection
    """

    oracle_home = module.params["oracle_home"]
    hostname = module.params["hostname"]
    port = module.params["port"]
    service_name = module.params["service_name"]
    sid = module.params["sid"]
    user = module.params["user"].lower()
    password = module.params["password"]
    mode = module.params["mode"].lower()

    if oracle_home is not None:
        os.environ['ORACLE_HOME'] = oracle_home.rstrip('/')
    elif 'ORACLE_HOME' in os.environ:
        oracle_home = os.environ['ORACLE_HOME']

    if sid:
        os.environ['ORACLE_SID'] = sid
    elif 'ORACLE_SID' in os.environ:
        sid = os.environ['ORACLE_SID']
        
    wallet_connect = '/@%s' % service_name
    sysdba_connect = '/' % service_name
    try:
        if not user and not password: # If neither user or password is supplied, the use of an oracle wallet is assumed
            if mode == 'sysdba':
                conn = cx_Oracle.connect(wallet_connect, mode=cx_Oracle.SYSDBA)
            else:
                conn = cx_Oracle.connect(wallet_connect)

        else user == 'sys' and mode == 'sysdba' and not password:
            conn = cx_Oracle.connect(sysdba_connect, mode=cx_Oracle.SYSDBA)
            
        elif (user and password ):
            if mode == 'sysdba':
                dsn = cx_Oracle.makedsn(host=hostname, port=port, service_name=service_name)
                connect = dsn
                conn = cx_Oracle.connect(user, password, dsn, mode=cx_Oracle.SYSDBA)
            else:
                dsn = cx_Oracle.makedsn(host=hostname, port=port, service_name=service_name)
                connect = dsn
                conn = cx_Oracle.connect(user, password, dsn)

        elif (not(user) or not(password)):
            module.fail_json(msg='Missing username or password for cx_Oracle')

    except cx_Oracle.DatabaseError as exc:
        error, = exc.args
        msg = 'Could not connect to database - %s, connect descriptor: %s' % (error.message, connect)
        module.fail_json(msg=msg, changed=False)

    return conn