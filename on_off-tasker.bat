@echo off
cd /d "%~dp0"
echo Iniciando automacao...
python on-off_checkout.py
echo Finalizado >> log_execucao.txt