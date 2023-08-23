# Configuração de Cluster Kubernetes On-Premises usando Pulumi

Este repositório contém um exemplo de como configurar um cluster Kubernetes em um servidor próprio (on-premises) usando o Pulumi.

## Pré-requisitos

- Conhecimento básico do Kubernetes e como ele funciona.
- Um servidor onde você deseja configurar o cluster Kubernetes.
- Pulumi instalado localmente.

## Configuração

1. Clone este repositório em seu ambiente local:

   ```sh
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
   ```

2. Configure seu ambiente Kubernetes:

Certifique-se de que seu servidor está pronto para executar um cluster Kubernetes. Isso pode envolver a instalação de dependências, como o Docker e o kubeadm.

Configurar o Pulumi:

Certifique-se de ter o Pulumi instalado. Caso contrário, siga as instruções em https://www.pulumi.com/docs/get-started/install/.

3. Personalizar a Configuração:

Abra o arquivo main.py e personalize as definições de implantação de acordo com suas necessidades.

4. Implantação do Cluster:

Execute o seguinte comando para implantar o cluster Kubernetes:

    ```sh
        pulumi up
    ```

5. Acessar o Cluster
   Depois de implantado, você pode acessar o cluster Kubernetes e interagir com ele usando as ferramentas de linha de comando do Kubernetes, como kubectl.
