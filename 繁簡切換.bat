@echo off
chcp 950 >nul

setlocal
:: ���U����| �� �ƭȦW��
set "regPath=HKEY_CURRENT_USER\SOFTWARE\Microsoft\IME\15.0\IMETC"
set "valueName=Enable Simplified Chinese Output"

:: �d�ߵ��U��(�T�O���o�ӭȪ��s�b)
for /f "tokens=5*" %%a in ('reg query "%regPath%" /v "%valueName%" 2^>nul') do (
    set "type=%%a"
    set "currentValue=%%b"
)

:: ��ܬd�ߵ��G
if defined currentValue (
    echo �d�ߵ��G
    echo ===================
    echo �ƭȦW��: %valueName%
    echo �ƭ�����: %type%
    echo �ƭȸ��: %currentValue%
    echo ===================
) else (
    echo �d�ߵ��G
    echo ===================
    echo �d�L %valueName%�C
    echo ===================

)

:: �ˬd��e�ƭȸ�ƨøӧ�
if "%currentValue%"=="0x00000001" (
    echo �������c�餤��
    reg add "%regPath%" /v "%valueName%" /t REG_SZ /d "0x00000000" /f
) else if "%currentValue%"=="0x00000000" (
    echo ������²�餤��
    reg add "%regPath%" /v "%valueName%" /t REG_SZ /d "0x00000001" /f
) else (
    echo �ƭȸ�Ʀ����D
)

pause

exit