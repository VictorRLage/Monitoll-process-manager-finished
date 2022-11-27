import psutil
import time
import colorama
import pyodbc
import textwrap
import subprocess
import datetime


global strip_SerialIdAtual
global strip3_OsAtual
global strip3_MaquinaAtual
global strip2_ProcessadorAtual
global strip2_DiscoAtual
global strip2_RamAtual
def func(value):
    return ''.join(value.splitlines())


try:
    # Bloco pegar serial id
    byte_SerialIdAtual = subprocess.check_output('''sudo dmidecode -s system-serial-number''', shell=True)
    str_SerialIdAtual = byte_SerialIdAtual.decode('UTF-8')
    strip_SerialIdAtual = str_SerialIdAtual.strip('\n')

    # Bloco pegar sistema operacional
    byte_OsAtual = subprocess.check_output('''lsb_release -d''', shell=True)
    str_OsAtual = byte_OsAtual.decode('UTF-8')
    strip_OsAtual = str_OsAtual.strip('Description:')
    strip2_OsAtual = strip_OsAtual.strip('\t')
    strip3_OsAtual = strip2_OsAtual.strip('\n')

    # Bloco pegar modelo maquina
    byte_MaquinaAtual = subprocess.check_output('''sudo dmidecode -t 1 | grep 'Product Name' | uniq''', shell=True)
    str_MaquinaAtual = byte_MaquinaAtual.decode('UTF-8')
    strip_MaquinaAtual = str_MaquinaAtual.strip('\tProduct')
    strip2_MaquinaAtual = strip_MaquinaAtual.strip(' Name: ')
    strip3_MaquinaAtual = strip2_MaquinaAtual.strip('\n')

    # Bloco pegar processador
    byte_ProcessadorAtual = subprocess.check_output('''lscpu | grep 'Model name:' | uniq''', shell=True)
    str_ProcessadorAtual = byte_ProcessadorAtual.decode('UTF-8')
    strip_ProcessadorAtual = str_ProcessadorAtual.strip('Model name:')
    strip2_ProcessadorAtual = strip_ProcessadorAtual.strip('\n')

    # Bloco pegar disco
    byte_DiscoAtual = subprocess.check_output('''sudo lshw -class disk -class storage | grep -B1 'vendor' | head -1''', shell=True)
    str_DiscoAtual = byte_DiscoAtual.decode('UTF-8')
    strip_DiscoAtual = str_DiscoAtual.strip('\tproduct: ')
    strip2_DiscoAtual = strip_DiscoAtual.strip('\n')

    # Bloco pegar velocidade da ram
    byte_RamAtual = subprocess.check_output('''sudo dmidecode --type memory | grep -B1 'Type Detail: ' | head -1''', shell=True)
    str_RamAtual = byte_RamAtual.decode('UTF-8')
    strip_RamAtual = str_RamAtual.strip('\tType: ')
    strip2_RamAtual = strip_RamAtual.strip('\n')
except:
    # CAPTURA SERIALID CMD
    direct_output2 = subprocess.check_output(
        'wmic bios get serialnumber', shell=True)
    SerialID = direct_output2.decode('UTF-8')
    trim1SerialID = SerialID.strip()
    trim2SerialID = func(trim1SerialID)
    trim3SerialID = trim2SerialID.strip("SerialNumber") 
    strip_SerialIdAtual = trim3SerialID.strip()


    # CAPTURA OS CMD
    direct_output6 = subprocess.check_output(
        'wmic os get Caption', shell=True)
    OSnome = direct_output6.decode('UTF-8')
    trim1OSnome = OSnome.strip()
    trim2OSnome = func(trim1OSnome)
    trim3OSnome = trim2OSnome.strip("Caption") 
    strip3_OsAtual = trim3OSnome.strip()



    # CAPTURA MODELO MAQUINA CMD
    direct_output = subprocess.check_output(
        'wmic computersystem get model', shell=True)
    modeloPC = direct_output.decode('UTF-8')
    trim1ModeloPC = modeloPC.strip()
    trim2ModeloPC = func(trim1ModeloPC)
    trim3ModeloPC = trim2ModeloPC.strip("Model") 
    strip3_MaquinaAtual = trim3ModeloPC.strip()



    # CAPTURA MODELO PROCESSADOR CMD
    direct_output3 = subprocess.check_output(
        'wmic cpu get name', shell=True)
    ModeloCPU = direct_output3.decode('UTF-8')
    trim1ModeloCPU = ModeloCPU.strip()
    trim2ModeloCPU = func(trim1ModeloCPU)
    trim3ModeloCPU = trim2ModeloCPU.strip("SerialNumber") 
    strip2_ProcessadorAtual = trim3ModeloCPU.strip()



    # CAPTURA MODELO DISCO CMD
    direct_output4 = subprocess.check_output(
        'wmic diskdrive get model', shell=True)
    ModeloDR = direct_output4.decode('UTF-8')
    trim1ModeloDR = ModeloDR.strip()
    trim2ModeloDR = func(trim1ModeloDR)
    trim3ModeloDR = trim2ModeloDR.strip("Model") 
    strip2_DiscoAtual = trim3ModeloDR.strip()



    # CAPTURA RAM SPEED CMD
    direct_output5 = subprocess.check_output(
        'wmic memorychip get speed', shell=True)
    ramSpeed = direct_output5.decode('UTF-8')
    trim1ramSpeed = ramSpeed.strip()
    trim2ramSpeed = func(trim1ramSpeed)
    trim3ramSpeed = trim2ramSpeed.strip("Speed") 
    strip2_RamAtual = trim3ramSpeed.strip()


# POGGERS BAR
def progress_bar(progresso, total, color=colorama.Fore.YELLOW):
    porcentagem = 100 * (progresso/float(total))
    barra = '█' * int(porcentagem) + '-' * (100 - int(porcentagem))
    print(color + f"\r|{barra}| {porcentagem:.2f}%", end="\r")
    if progresso == total:
        print(colorama.Fore.GREEN +
              f"\r|{barra}| {porcentagem:.2f}%", end="\r")

# conexao com banco


def Conexao():

    try:
        # variaveis de conexao
        driver = '{ODBC Driver 18 for SQL Server}'
        server_name = 'montioll'
        database_name = 'Monitoll'
        server = '{server_name}.database.windows.net,1433'.format(
            server_name=server_name)
        username = 'Monitoll'
        password = 'Grupo7@123'
        # definindo banco url
        connection_string = textwrap.dedent('''
            Driver={driver};
            Server={server};
            Database={database};
            Uid={username};
            Pwd={password};
            Encrypt=yes;
            TrustedServerCertificate=no;
            Connection Timeout=10;
            '''.format(
            driver=driver,
            server=server,
            database=database_name,
            username=username,
            password=password
        ))

        cnxn: pyodbc.Connection = pyodbc.connect(connection_string)

        global crsr
        crsr = cnxn.cursor()
        print("Conectado ao banco de dados!")
        Login()
    except pyodbc.Error as err:
        print("Something went wrong: {}".format(err))
        print("Conexão com a Azure perdida!")
        print("Por favor restabeleça conexão com a internet ou tente novamente mais tarde!")


def Login():

    print("Bem vindo ao Grenn Light - Task Manager!")
    print("Login")
    u_email = 'kaique@gmail.com'#input('Seu e-mail: ')
    u_senha = '123'#input('Sua senha: ')
    ValidarLogin(u_email, u_senha)


def ValidarLogin(email, senha):

    try:
        crsr.execute('''
        SELECT Nome,fkEmpresa FROM Usuario WHERE Email = ? and Senha = ?
        ''', email, senha)
        global usuario
        usuario = crsr.fetchall()
        print("Login efetuado com sucesso")
        u_usuario = usuario[0]
        print(f'Bem vindo {u_usuario[0]}!')
        global fkEmpresa
        fkEmpresa = u_usuario[1]
        BuscarTorres(fkEmpresa)

    except pyodbc.Error as err:
        print("Something went wrong: {}".format(err))
        print("Falha ao realizar login por favor tente novamente")


def BuscarTorres(fkEmpresa):

    try:
        crsr.execute('''
    SELECT idTorre FROM Torre WHERE fkEmpresa = ?
    ''', fkEmpresa)
        # Executando comando SQL)
        idTorres = crsr.fetchall()
        EscolherTorres(idTorres)

    except pyodbc.Error as err:
        print("Something went wrong: {}".format(err))
        print('Sua empresa não possui torres no nosso sistema.')
        print('Por favor entre em contato conosco atraves do nosso site!')


def EscolherTorres(idTorres):
    for x in idTorres:
        print('Maquina:', x[0])
    idTorre = '162'#input('Qual é esta maquina? ')
    BuscarComponentes(idTorre)

def BuscarComponentes(idTorre):

    # PEGAR fkCOMPONENTE
    try:
        crsr.execute('''
        SELECT fkComponente FROM Torre_Componente WHERE Torre_Componente.fkTorre = ?
        ''', idTorre)
        fkComponentes = crsr.fetchall()
        idProcessos = True
        for x in fkComponentes:
            if x[0] == 25:
                idProcessos = True
                VerificarDadosMaquina(idTorre)
        if not idProcessos:
            print('Você não selecionou a captura de processos como parte do seu plano para esta maquina.')
            print('Por favor entre em contato com a gente para aumentar seu plano!')

    except pyodbc.Error as err:
        print("Something went wrong: {}".format(err))


def VerificarDadosMaquina(idTorre):

    try:
        crsr.execute('''
        SELECT SerialID FROM Torre WHERE idTorre = ?
        ''', idTorre)
        # Executando comando SQL
        print("Verificando dados da torre...")
        SerialIdBanco = crsr.fetchone()

    except pyodbc.Error as err:
        print("Something went wrong: {}".format(err))
        print("Não foi possivel verificar os dados da maquina.")
        print("Por favor tente novamente mais tarde!")

    if SerialIdBanco[0] != '':
        print("A torre possui dados cadastrados")
        CapturarLeitura(idTorre)
    else:
        print("A torre não possui dados")
        InserirDadosMaquina(strip_SerialIdAtual, strip3_OsAtual, strip3_MaquinaAtual,
                            strip2_ProcessadorAtual, strip2_DiscoAtual, strip2_RamAtual, idTorre)
        
def InserirDadosMaquina(SerialID, OS, Maquina, Processador, Disco, RamSpeed, idTorre):

    try:
        crsr.execute('''
        UPDATE Torre  SET SerialID = ?,  SO = ?, Maquina = ?, Processador = ?, Disco = ?, Ram = ?,  fkEmpresa = ? WHERE idTorre = ?
        ''', SerialID, OS, Maquina, Processador, Disco, RamSpeed, fkEmpresa, idTorre)
        # Executando comando SQL
        # Commit de mudanças no banco de dados
        crsr.commit()
        print("Dados da maquina cadastrados!")
        CapturarLeitura(idTorre)

    except pyodbc.Error as err:
        crsr.rollback()
        print("Something went wrong: {}".format(err))
        print("Não foi possivel cadastrar os dados da maquina.")
        print("Por favor tente novamente mais tarde!")

def CapturarLeitura(idTorre):
    while True:
        json_dados = []
        array_pids = []
        for proc in psutil.process_iter(['pid']):
            array_pids.append(proc.pid)


        # print(array_pids)
        # print(len(array_pids))

        print('Iniciando Leitura!')
        nucleos = psutil.cpu_count()

        # print("NOME | PID | STATUS | USO CPU | USO RAM")
        for i, proc in enumerate(psutil.process_iter()):
            n = proc.name()
            p = proc.ppid()
            s = proc.status()
            c = float(proc.cpu_percent(interval=1)/nucleos)
            m = proc.memory_percent()
            d = datetime.datetime.fromtimestamp(proc.create_time()).strftime("%Y-%m-%d %H:%M:%S")
            nao = "n"
            json_dados.append('{"name":c, "pid":p, "status":s, "usoCpu":c, "usoRam":m, "dataCriacao":d, "confiavel":nao}')

            # print(f"{n} | {p} | {s} | {c:.2f}% | {m:.2f}%")
            progress_bar(i+1, len(array_pids))
        progress_bar(1, 1)

        print(colorama.Fore.RESET)
        print(f"\r")
        VerificarProcessos(idTorre,json_dados)
        # AtualizarProcessos(idTorre,json_dados)
        time.sleep(30)

def VerificarProcessos(idTorre,json_dados):
    lenDados = len(json_dados)
    print(lenDados)
    print(idTorre)
    try:
        crsr.execute('''
        SELECT TOP (?) * FROM Processo WHERE fkTorre = ? ORDER BY idProcesso DESC
        ''', idTorre, idTorre)
        array_proc = crsr.fetchall()
        print('pinto')
        print(array_proc)
        print('pinto')

    except pyodbc.Error as err:
        print('erro aqui')
        print("Something went wrong: {}".format(err))



Conexao()





