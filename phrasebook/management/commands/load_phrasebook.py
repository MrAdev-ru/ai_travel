"""
Management command to load sample phrasebook data.
Usage: python manage.py load_phrasebook
"""
from django.core.management.base import BaseCommand
from phrasebook.models import PhraseCategory, Phrase


# Sample travel phrases organized by category with multi-language translations
PHRASEBOOK_DATA = [
    {
        'name': 'Airport',
        'slug': 'airport',
        'icon': 'bi-airplane',
        'description': 'Essential phrases for navigating airports and flights',
        'order': 1,
        'phrases': [
            {
                'source_text': 'Where is the check-in counter?',
                'pronunciation': '',
                'translations': {
                    'es': '¿Dónde está el mostrador de facturación?',
                    'fr': 'Où est le comptoir d\'enregistrement?',
                    'de': 'Wo ist der Check-in-Schalter?',
                    'ja': 'チェックインカウンターはどこですか？',
                    'ar': 'أين توجد مكتب تسجيل الوصول؟',
                    'zh': '值机柜台在哪里？',
                },
            },
            {
                'source_text': 'I have a reservation.',
                'translations': {
                    'es': 'Tengo una reserva.',
                    'fr': 'J\'ai une réservation.',
                    'de': 'Ich habe eine Reservierung.',
                    'ja': '予約があります。',
                    'ar': 'لدي حجز.',
                    'zh': '我有预订。',
                },
            },
            {
                'source_text': 'Where is my gate?',
                'translations': {
                    'es': '¿Dónde está mi puerta de embarque?',
                    'fr': 'Où est ma porte d\'embarquement?',
                    'de': 'Wo ist mein Gate?',
                    'ja': '搭乗ゲートはどこですか？',
                    'ar': 'أين بوابة المغادرة؟',
                    'zh': '我的登机口在哪里？',
                },
            },
            {
                'source_text': 'Is the flight on time?',
                'translations': {
                    'es': '¿El vuelo sale a tiempo?',
                    'fr': 'Le vol est-il à l\'heure?',
                    'de': 'Ist der Flug pünktlich?',
                    'ja': '便は定刻ですか？',
                    'ar': 'هل الرحلة في الموعد؟',
                    'zh': '航班准时吗？',
                },
            },
            {
                'source_text': 'Where can I collect my baggage?',
                'translations': {
                    'es': '¿Dónde puedo recoger mi equipaje?',
                    'fr': 'Où puis-je récupérer mes bagages?',
                    'de': 'Wo kann ich mein Gepäck abholen?',
                    'ja': '荷物はどこで受け取れますか？',
                    'ar': 'أين يمكنني استلام أمتعتي؟',
                    'zh': '在哪里取行李？',
                },
            },
            {
                'source_text': 'I need to declare something.',
                'translations': {
                    'es': 'Necesito declarar algo.',
                    'fr': 'Je dois déclarer quelque chose.',
                    'de': 'Ich muss etwas deklarieren.',
                    'ja': '申告するものがあります。',
                    'ar': 'أحتاج إلى الإقرار بشيء.',
                    'zh': '我需要申报物品。',
                },
            },
        ],
    },
    {
        'name': 'Hotel',
        'slug': 'hotel',
        'icon': 'bi-building',
        'description': 'Phrases for hotel check-in, services, and requests',
        'order': 2,
        'phrases': [
            {
                'source_text': 'I have a reservation under the name...',
                'translations': {
                    'es': 'Tengo una reserva a nombre de...',
                    'fr': 'J\'ai une réservation au nom de...',
                    'de': 'Ich habe eine Reservierung auf den Namen...',
                    'ja': '...の名前で予約しています。',
                    'ar': 'لدي حجز باسم...',
                    'zh': '我以...的名字预订了房间。',
                },
            },
            {
                'source_text': 'What time is check-out?',
                'translations': {
                    'es': '¿A qué hora es el check-out?',
                    'fr': 'À quelle heure est le départ?',
                    'de': 'Wann ist der Check-out?',
                    'ja': 'チェックアウトは何時ですか？',
                    'ar': 'متى موعد المغادرة؟',
                    'zh': '退房时间是几点？',
                },
            },
            {
                'source_text': 'Can I have an extra towel, please?',
                'translations': {
                    'es': '¿Puedo tener una toalla extra, por favor?',
                    'fr': 'Puis-je avoir une serviette supplémentaire?',
                    'de': 'Kann ich bitte ein extra Handtuch haben?',
                    'ja': 'タオルを追加でもらえますか？',
                    'ar': 'هل يمكنني الحصول على منشفة إضافية؟',
                    'zh': '请再给我一条毛巾。',
                },
            },
            {
                'source_text': 'The air conditioning is not working.',
                'translations': {
                    'es': 'El aire acondicionado no funciona.',
                    'fr': 'La climatisation ne fonctionne pas.',
                    'de': 'Die Klimaanlage funktioniert nicht.',
                    'ja': 'エアコンが動きません。',
                    'ar': 'المكيف لا يعمل.',
                    'zh': '空调坏了。',
                },
            },
            {
                'source_text': 'Is breakfast included?',
                'translations': {
                    'es': '¿Está incluido el desayuno?',
                    'fr': 'Le petit-déjeuner est-il inclus?',
                    'de': 'Ist das Frühstück inbegriffen?',
                    'ja': '朝食は含まれていますか？',
                    'ar': 'هل الإفطار مشمول؟',
                    'zh': '包含早餐吗？',
                },
            },
            {
                'source_text': 'Can you call a taxi for me?',
                'translations': {
                    'es': '¿Puede llamar un taxi por mí?',
                    'fr': 'Pouvez-vous appeler un taxi pour moi?',
                    'de': 'Können Sie ein Taxi für mich rufen?',
                    'ja': 'タクシーを呼んでもらえますか？',
                    'ar': 'هل يمكنك طلب تاكسي لي؟',
                    'zh': '能帮我叫辆出租车吗？',
                },
            },
        ],
    },
    {
        'name': 'Restaurant',
        'slug': 'restaurant',
        'icon': 'bi-cup-hot',
        'description': 'Ordering food and dining out phrases',
        'order': 3,
        'phrases': [
            {
                'source_text': 'A table for two, please.',
                'translations': {
                    'es': 'Una mesa para dos, por favor.',
                    'fr': 'Une table pour deux, s\'il vous plaît.',
                    'de': 'Einen Tisch für zwei, bitte.',
                    'ja': '二人席をお願いします。',
                    'ar': 'طاولة لشخصين، من فضلك.',
                    'zh': '请给我们两人桌。',
                },
            },
            {
                'source_text': 'Can I see the menu, please?',
                'translations': {
                    'es': '¿Puedo ver el menú, por favor?',
                    'fr': 'Puis-je voir le menu, s\'il vous plaît?',
                    'de': 'Kann ich bitte die Speisekarte sehen?',
                    'ja': 'メニューを見せてください。',
                    'ar': 'هل يمكنني رؤية قائمة الطعام؟',
                    'zh': '请给我菜单。',
                },
            },
            {
                'source_text': 'I am allergic to nuts.',
                'translations': {
                    'es': 'Soy alérgico a los frutos secos.',
                    'fr': 'Je suis allergique aux noix.',
                    'de': 'Ich bin allergisch gegen Nüsse.',
                    'ja': 'ナッツアレルギーがあります。',
                    'ar': 'لدي حساسية من المكسرات.',
                    'zh': '我对坚果过敏。',
                },
            },
            {
                'source_text': 'The bill, please.',
                'translations': {
                    'es': 'La cuenta, por favor.',
                    'fr': 'L\'addition, s\'il vous plaît.',
                    'de': 'Die Rechnung, bitte.',
                    'ja': 'お会計お願いします。',
                    'ar': 'الفاتورة، من فضلك.',
                    'zh': '请结账。',
                },
            },
            {
                'source_text': 'Is the tip included?',
                'translations': {
                    'es': '¿Está incluida la propina?',
                    'fr': 'Le pourboire est-il inclus?',
                    'de': 'Ist das Trinkgeld inbegriffen?',
                    'ja': 'チップは含まれていますか？',
                    'ar': 'هل البقشيش مشمول؟',
                    'zh': '包含小费吗？',
                },
            },
            {
                'source_text': 'This is delicious!',
                'translations': {
                    'es': '¡Está delicioso!',
                    'fr': 'C\'est délicieux!',
                    'de': 'Das ist köstlich!',
                    'ja': 'おいしいです！',
                    'ar': 'هذا لذيذ!',
                    'zh': '太好吃了！',
                },
            },
        ],
    },
    {
        'name': 'Taxi',
        'slug': 'taxi',
        'icon': 'bi-taxi-front',
        'description': 'Getting around by taxi and public transport',
        'order': 4,
        'phrases': [
            {
                'source_text': 'Please take me to this address.',
                'translations': {
                    'es': 'Por favor, lléveme a esta dirección.',
                    'fr': 'Veuillez me conduire à cette adresse.',
                    'de': 'Bitte fahren Sie mich zu dieser Adresse.',
                    'ja': 'この住所までお願いします。',
                    'ar': 'من فضلك خذني إلى هذا العنوان.',
                    'zh': '请带我去这个地址。',
                },
            },
            {
                'source_text': 'How much will it cost?',
                'translations': {
                    'es': '¿Cuánto costará?',
                    'fr': 'Combien cela coûtera-t-il?',
                    'de': 'Wie viel wird es kosten?',
                    'ja': 'いくらかかりますか？',
                    'ar': 'كم سيكلف؟',
                    'zh': '要多少钱？',
                },
            },
            {
                'source_text': 'Can you turn on the meter, please?',
                'translations': {
                    'es': '¿Puede encender el taxímetro, por favor?',
                    'fr': 'Pouvez-vous allumer le compteur, s\'il vous plaît?',
                    'de': 'Können Sie bitte den Taxameter einschalten?',
                    'ja': 'メーターを入れてください。',
                    'ar': 'هل يمكنك تشغيل العداد؟',
                    'zh': '请打表。',
                },
            },
            {
                'source_text': 'Please stop here.',
                'translations': {
                    'es': 'Por favor, pare aquí.',
                    'fr': 'Arrêtez-vous ici, s\'il vous plaît.',
                    'de': 'Bitte halten Sie hier.',
                    'ja': 'ここで止めてください。',
                    'ar': 'من فضلك توقف هنا.',
                    'zh': '请在这里停。',
                },
            },
            {
                'source_text': 'How long will it take?',
                'translations': {
                    'es': '¿Cuánto tiempo tardará?',
                    'fr': 'Combien de temps cela prendra-t-il?',
                    'de': 'Wie lange wird es dauern?',
                    'ja': 'どのくらいかかりますか？',
                    'ar': 'كم من الوقت سيستغرق؟',
                    'zh': '需要多长时间？',
                },
            },
            {
                'source_text': 'Do you accept credit cards?',
                'translations': {
                    'es': '¿Aceptan tarjetas de crédito?',
                    'fr': 'Acceptez-vous les cartes de crédit?',
                    'de': 'Akzeptieren Sie Kreditkarten?',
                    'ja': 'クレジットカードは使えますか？',
                    'ar': 'هل تقبلون بطاقات الائتمان؟',
                    'zh': '可以刷卡吗？',
                },
            },
        ],
    },
    {
        'name': 'Shopping',
        'slug': 'shopping',
        'icon': 'bi-bag',
        'description': 'Shopping and bargaining phrases',
        'order': 5,
        'phrases': [
            {
                'source_text': 'How much does this cost?',
                'translations': {
                    'es': '¿Cuánto cuesta esto?',
                    'fr': 'Combien coûte ceci?',
                    'de': 'Wie viel kostet das?',
                    'ja': 'これはいくらですか？',
                    'ar': 'كم يكلف هذا؟',
                    'zh': '这个多少钱？',
                },
            },
            {
                'source_text': 'Do you have this in a different size?',
                'translations': {
                    'es': '¿Tiene esto en otra talla?',
                    'fr': 'Avez-vous ceci dans une autre taille?',
                    'de': 'Haben Sie das in einer anderen Größe?',
                    'ja': '別のサイズはありますか？',
                    'ar': 'هل لديكم هذا بمقاس مختلف؟',
                    'zh': '有其他尺码吗？',
                },
            },
            {
                'source_text': 'Can I try this on?',
                'translations': {
                    'es': '¿Puedo probármelo?',
                    'fr': 'Puis-je l\'essayer?',
                    'de': 'Kann ich das anprobieren?',
                    'ja': '試着できますか？',
                    'ar': 'هل يمكنني تجربته؟',
                    'zh': '我可以试穿吗？',
                },
            },
            {
                'source_text': 'Is there a discount?',
                'translations': {
                    'es': '¿Hay descuento?',
                    'fr': 'Y a-t-il une réduction?',
                    'de': 'Gibt es einen Rabatt?',
                    'ja': '割引はありますか？',
                    'ar': 'هل هناك خصم؟',
                    'zh': '有折扣吗？',
                },
            },
            {
                'source_text': 'I am just looking, thank you.',
                'translations': {
                    'es': 'Solo estoy mirando, gracias.',
                    'fr': 'Je regarde seulement, merci.',
                    'de': 'Ich schaue nur, danke.',
                    'ja': '見ているだけです、ありがとう。',
                    'ar': 'أنا فقط أتفرج، شكراً.',
                    'zh': '我只是看看，谢谢。',
                },
            },
            {
                'source_text': 'Can I pay by card?',
                'translations': {
                    'es': '¿Puedo pagar con tarjeta?',
                    'fr': 'Puis-je payer par carte?',
                    'de': 'Kann ich mit Karte bezahlen?',
                    'ja': 'カードで払えますか？',
                    'ar': 'هل يمكنني الدفع بالبطاقة؟',
                    'zh': '可以刷卡吗？',
                },
            },
        ],
    },
    {
        'name': 'Emergency',
        'slug': 'emergency',
        'icon': 'bi-hospital',
        'description': 'Critical phrases for emergencies and medical situations',
        'order': 6,
        'phrases': [
            {
                'source_text': 'Help!',
                'translations': {
                    'es': '¡Ayuda!',
                    'fr': 'Au secours!',
                    'de': 'Hilfe!',
                    'ja': '助けて！',
                    'ar': 'النجدة!',
                    'zh': '救命！',
                },
            },
            {
                'source_text': 'Call an ambulance!',
                'translations': {
                    'es': '¡Llame a una ambulancia!',
                    'fr': 'Appelez une ambulance!',
                    'de': 'Rufen Sie einen Krankenwagen!',
                    'ja': '救急車を呼んでください！',
                    'ar': 'اتصل بسيارة الإسعاف!',
                    'zh': '叫救护车！',
                },
            },
            {
                'source_text': 'I need a doctor.',
                'translations': {
                    'es': 'Necesito un médico.',
                    'fr': 'J\'ai besoin d\'un médecin.',
                    'de': 'Ich brauche einen Arzt.',
                    'ja': '医者が必要です。',
                    'ar': 'أحتاج طبيباً.',
                    'zh': '我需要医生。',
                },
            },
            {
                'source_text': 'Where is the nearest hospital?',
                'translations': {
                    'es': '¿Dónde está el hospital más cercano?',
                    'fr': 'Où est l\'hôpital le plus proche?',
                    'de': 'Wo ist das nächste Krankenhaus?',
                    'ja': '最寄りの病院はどこですか？',
                    'ar': 'أين أقرب مستشفى؟',
                    'zh': '最近的医院在哪里？',
                },
            },
            {
                'source_text': 'I lost my passport.',
                'translations': {
                    'es': 'Perdí mi pasaporte.',
                    'fr': 'J\'ai perdu mon passeport.',
                    'de': 'Ich habe meinen Reisepass verloren.',
                    'ja': 'パスポートをなくしました。',
                    'ar': 'فقدت جواز سفري.',
                    'zh': '我的护照丢了。',
                },
            },
            {
                'source_text': 'Please call the police.',
                'translations': {
                    'es': 'Por favor, llame a la policía.',
                    'fr': 'Appelez la police, s\'il vous plaît.',
                    'de': 'Bitte rufen Sie die Polizei.',
                    'ja': '警察を呼んでください。',
                    'ar': 'من فضلك اتصل بالشرطة.',
                    'zh': '请报警。',
                },
            },
        ],
    },
]


class Command(BaseCommand):
    help = 'Load sample phrasebook categories and phrases'

    def handle(self, *args, **options):
        created_categories = 0
        created_phrases = 0

        for cat_data in PHRASEBOOK_DATA:
            phrases_data = cat_data.pop('phrases', [])
            category, created = PhraseCategory.objects.update_or_create(
                slug=cat_data['slug'],
                defaults=cat_data,
            )
            if created:
                created_categories += 1

            for idx, phrase_data in enumerate(phrases_data):
                _, p_created = Phrase.objects.update_or_create(
                    category=category,
                    source_text=phrase_data['source_text'],
                    defaults={
                        'translations': phrase_data.get('translations', {}),
                        'pronunciation': phrase_data.get('pronunciation', ''),
                        'order': idx,
                    },
                )
                if p_created:
                    created_phrases += 1

        self.stdout.write(
            self.style.SUCCESS(
                f'Phrasebook loaded: {created_categories} categories, {created_phrases} phrases created.'
            )
        )
