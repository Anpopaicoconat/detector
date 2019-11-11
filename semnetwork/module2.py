import nltk
strin='''Внизу у деревянной галерейки, приделанной к наружной стене ограды, толпились на этот раз всё женщины, баб около двадцати. Их уведомили, что старец наконец выйдет, и они собрались в ожидании. Вышли на галерейку и помещицы Хохлаковы, тоже ожидавшие старца, но в отведенном для благородных посетительниц помещении. Их было две: мать и дочь. Госпожа Хохлакова-мать, дама богатая и всегда со вкусом одетая, была еще довольно молодая и очень миловидная собою особа, немного бледная, с очень оживленными и почти совсем черными глазами. Ей было не более тридцати трех лет, и она уже лет пять как была вдовой. Четырнадцатилетняя дочь ее страдала параличом ног. Бедная девочка не могла ходить уже с полгода, и ее возили в длинном покойном кресле на колесах. Это было прелестное личико, немного худенькое от болезни, но веселое. Что-то шаловливое светилось в ее темных больших глазах с длинными ресницами. Мать еще с весны собиралась ее везти за границу, но летом опоздали за устройством по имению. Они уже с неделю как жили в нашем городе, больше по делам, чем для богомолья, но уже раз, три дня тому назад, посещали старца. Теперь они приехали вдруг опять, хотя и знали, что старец почти уже не может вовсе никого принимать, и, настоятельно умоляя, просили еще раз «счастья узреть великого исцелителя»
В ожидании выхода старца мамаша сидела на стуле, подле кресел дочери, а в двух шагах от нее стоял старик монах, не из здешнего монастыря, а захожий из одной дальней северной малоизвестной обители. Он тоже желал благословиться у старца. Но показавшийся на галерее старец прошел сначала прямо к народу. Толпа затеснилась к крылечку о трех ступеньках, соединявшему низенькую галерейку с полем. Старец стал на верхней ступеньке, надел эпитрахиль и начал благословлять теснившихся к нему женщин. Притянули к нему одну кликушу за обе руки. Та, едва лишь завидела старца, вдруг начала, как-то нелепо взвизгивая, икать и вся затряслась, как в родимце. Наложив ей на голову эпитрахиль, старец прочел над нею краткую молитву, и она тотчас затихла и успокоилась. Не знаю, как теперь, но в детстве моем мне часто случалось в деревнях и по монастырям видеть и слышать этих кликуш. Их приводили к обедне, они визжали или лаяли по-собачьи на всю церковь, но, когда выносили дары и их подводили к дарам, тотчас «беснование» прекращалось и больные на несколько времени всегда успокоивались. Меня, ребенка, очень это поражало и удивляло. Но тогда же я услышал от иных помещиков и особенно от городских учителей моих, на мои расспросы, что это всё притворство, чтобы не работать, и что это всегда можно искоренить надлежащею строгостью, причем приводились для подтверждения разные анекдоты. Но впоследствии я с удивлением узнал от специалистов-медиков, что тут никакого нет притворства, что это страшная женская болезнь, и кажется, по преимуществу у нас на Руси, свидетельствующая о тяжелой судьбе нашей сельской женщины, болезнь, происходящая от изнурительных работ слишком вскоре после тяжелых, неправильных, безо всякой медицинской помощи родов; кроме того, от безвыходного горя, от побоев и проч., чего иные женские натуры выносить по общему примеру все-таки не могут. Странное же и мгновенное исцеление беснующейся и бьющейся женщины, только лишь, бывало, ее подведут к дарам, которое объясняли мне притворством и сверх того фокусом, устраиваемым чуть ли не самими «клерикалами», происходило, вероятно, тоже самым натуральным образом, и подводившие ее к дарам бабы, а главное, и сама больная, вполне веровали, как установившейся истине, что нечистый дух, овладевший больною, никогда не может вынести, если ее, больную, подведя к дарам, наклонят пред ними. А потому и всегда происходило (и должно было происходить) в нервной и, конечно, тоже психически больной женщине непременное как бы сотрясение всего организма ее в момент преклонения пред дарами, сотрясение, вызванное ожиданием непременного чуда исцеления и самою полною верой в то, что оно совершится. И оно совершалось хотя бы только на одну минуту. Точно так же оно и теперь совершилось, едва лишь старец накрыл больную эпитрахилью.
Многие из теснившихся к нему женщин заливались слезами умиления и восторга, вызванного эффектом минуты; другие рвались облобызать хоть край одежды его, иные что-то причитали. Он благословлял всех, а с иными разговаривал. Кликушу он уже знал, ее привели не издалека, из деревни всего верст за шесть от монастыря, да и прежде водили к нему.
— А вот далекая! — указал он на одну еще вовсе не старую женщину, но очень худую и испитую, не то что загоревшую, а как бы всю почерневшую лицом. Она стояла на коленях и неподвижным взглядом смотрела на старца. Во взгляде ее было что-то как бы исступленное.
— Издалека, батюшка, издалека, отселева триста верст. Издалека, отец, издалека, — проговорила женщина нараспев, как-то покачивая плавно из стороны в сторону головой и подпирая щеку ладонью. Говорила она как бы причитывая. Есть в народе горе молчаливое и многотерпеливое; оно уходит в себя и молчит. Но есть горе и надорванное: оно пробьется раз слезами и с той минуты уходит в причитывания. Это особенно у женщин. Но не легче оно молчаливого горя. Причитания утоляют тут лишь тем, что еще более растравляют и надрывают сердце. Такое горе и утешения не желает, чувством своей неутолимости питается. Причитания лишь потребность раздражать беспрерывно рану.
— По мещанству, надоть быть? — продолжал, любопытно в нее вглядываясь, старец.
— Городские мы, отец, городские, по крестьянству мы, а городские, в городу проживаем. Тебя повидать, отец, прибыла. Слышали о тебе, батюшка, слышали. Сыночка младенчика схоронила, пошла молить бога. В трех монастырях побывала, да указали мне: «Зайди, Настасьюшка, и сюда, к вам то есть, голубчик, к вам». Пришла, вчера у стояния была, а сегодня и к вам.
— О чем плачешь-то?
— Сыночка жаль, батюшка, трехлеточек был, без трех только месяцев и три бы годика ему. По сыночку мучусь, отец, по сыночку. Последний сыночек оставался, четверо было у нас с Никитушкой, да не стоят у нас детушки, не стоят, желанный, не стоят. Трех первых схоронила я, не жалела я их очень-то, а этого последнего схоронила и забыть его не могу. Вот точно он тут предо мной стоит, не отходит. Душу мне иссушил. Посмотрю на его бельишечко, на рубашоночку аль на сапожки и взвою. Разложу, что после него осталось, всякую вещь его, смотрю и вою. Говорю Никитушке, мужу-то моему: отпусти ты меня, хозяин, на богомолье сходить. Извозчик он, не бедные мы, отец, не бедные, сами от себя извоз ведем, всё свое содержим, и лошадок и экипаж. Да на что теперь нам добро? Зашибаться он стал без меня, Никитушка-то мой, это наверно что так, да и прежде того: чуть я отвернусь, а уж он и ослабеет. А теперь и о нем не думаю. Вот уж третий месяц из дому. Забыла я, обо всем забыла и помнить не хочу; а и что я с ним теперь буду? Кончила я с ним, кончила, со всеми покончила. И не глядела бы я теперь на свой дом и на свое добро, и не видала б я ничего вовсе!
— Вот что, мать, — проговорил старец, — однажды древний великий святой увидел во храме такую же, как ты, плачущую мать и тоже по младенце своем, по единственном, которого тоже призвал господь. «Или не знаешь ты, — сказал ей святой, — сколь сии младенцы пред престолом божиим дерзновенны? Даже и нет никого дерзновеннее их в царствии небесном: ты, господи, даровал нам жизнь, говорят они богу, и только лишь мы узрели ее, как ты ее у нас и взял назад. И столь дерзновенно просят и спрашивают, что господь дает им немедленно ангельский чин. А посему, — молвил святой, — и ты радуйся, жено, а не плачь, и твой младенец теперь у господа в сонме ангелов его пребывает». Вот что сказал святой плачущей жене в древние времена. Был же он великий святой и неправды ей поведать не мог. Посему знай и ты, мать, что и твой младенец наверно теперь предстоит пред престолом господним, и радуется, и веселится, и о тебе бога молит. А потому и ты плачь, но радуйся.
Женщина слушала его, подпирая рукой щеку и потупившись. Она глубоко вздохнула.
— Тем самым и Никитушка меня утешал, в одно слово, как ты, говорил: «Неразумная ты, говорит, чего плачешь, сыночек наш наверно теперь у господа бога вместе с ангелами воспевает». Говорит он это мне, а и сам плачет, вижу я, как и я же, плачет «Знаю я, говорю, Никитушка, где ж ему и быть, коль не у господа бога, только здесь-то, с нами-то его теперь, Никитушка, нет, подле-то, вот как прежде сидел!» И хотя бы я только взглянула на него лишь разочек, только один разочек на него мне бы опять поглядеть, и не подошла бы к нему, не промолвила, в углу бы притаилась, только бы минуточку едину повидать, послыхать его, как он играет на дворе, придет, бывало, крикнет своим голосочком: «Мамка, где ты?» Только б услыхать-то мне, как он по комнате своими ножками пройдет разик, всего бы только разик, ножками-то своими тук-тук, да так часто часто, помню, как, бывало, бежит ко мне, кричит да смеется, только б я его ножки-то услышала, услышала бы, признала! Да нет его, батюшка, нет, и не услышу его никогда! Вот его поясочек, а его-то и нет, и никогда-то мне теперь не видать, не слыхать его!..
Она вынула из-за пазухи маленький позументный поясочек своего мальчика и, только лишь взглянула на него, так и затряслась от рыданий, закрыв пальцами глаза свои, сквозь которые потекли вдруг брызнувшие ручьем слезы
— А это, — проговорил старец, это древняя «Рахиль плачет о детях своих и не может утешиться, потому что их нет», и таковой вам, матерям, предел на земле положен. И не утешайся, и не надо тебе утешаться, не утешайся и плачь, только каждый раз, когда плачешь, вспоминай неуклонно, что сыночек твой — есть единый от ангелов божиих — оттуда на тебя смотрит и видит тебя, и на твои слезы радуется, и на них господу богу указывает. И надолго еще тебе сего великого материнского плача будет, но обратится он под конец тебе в тихую радость, и будут горькие слезы твои лишь слезами тихого умиления и сердечного очищения, от грехов спасающего. А младенчика твоего помяну за упокой, как звали-то?
— Алексеем, батюшка.
— Имя-то милое. На Алексея человека божия?
— Божия, батюшка, божия, Алексея человека божия!
Святой-то какой! Помяну, мать, помяну и печаль твою на молитве вспомяну и супруга твоего за здравие помяну. Только его тебе грех оставлять. Ступай к мужу и береги его. Увидит оттуда твой мальчик, что бросила ты его отца, и заплачет по вас; зачем же ты блаженство-то его нарушаешь? Ведь жив он, жив, ибо жива душа вовеки; и нет его в доме, а он невидимо подле вас. Как же он в дом придет, коль ты говоришь, что возненавидела дом свой? К кому ж он придет, коль вас вместе, отца с матерью, не найдет? Вот он снится теперь тебе, и ты мучаешься, а тогда он тебе кроткие сны пошлет. Ступай к мужу, мать, сего же дня ступай.
— Пойду, родной, по твоему слову пойду. Сердце ты мое разобрал. Никитушка, ты мой Никитушка, ждешь ты меня, голубчик, ждешь! — начала было причитывать баба, но старец уже обратился к одной старенькой старушонке, одетой не по-страннически, а по-городски. По глазам ее видно было, что у нее какое-то дело и что пришла она нечто сообщить. Назвалась она унтер-офицерскою вдовой, не издалека, всего из нашего же города. Сыночек у ней Васенька, где-то в комиссариате служил, да в Сибирь поехал, в Иркутск. Два раза оттуда писал, а тут вот уже год писать перестал. Справлялась она о нем, да, по правде, не знает, где и справиться-то.
— Только и говорит мне намедни Степанида Ильинишна Бедрягина, купчиха она, богатая: возьми ты, говорит, Прохоровна, и запиши ты, говорит, сыночка своего в поминанье, снеси в церковь, да и помяни за упокой. Душа-то его, говорит, затоскует, он и напишет письмо. «И это, — говорит Степанида Ильинишна, — как есть верно, многократно испытано». Да только я сумлеваюсь... Свет ты наш, правда оно аль неправда, и хорошо ли так будет?
— И не думай о сем. Стыдно это и спрашивать. Да и как это возможно, чтобы живую душу да еще родная мать за упокой поминала! Это великий грех, колдовству подобно, только по незнанию твоему лишь прощается. А ты лучше помоли царицу небесную, скорую заступницу и помощницу, о здоровье его, да чтоб и тебя простила за неправильное размышление твое. И вот что я тебе еще скажу, Прохоровна: или сам он к тебе вскоре обратно прибудет, сынок твой, или наверно письмо пришлет. Так ты и знай. Ступай и отселе покойна будь. Жив твой сынок, говорю тебе.
— Милый ты наш, награди тебя бог, благодетель ты наш, молебщик ты за всех нас и за грехи наши...
А старец уже заметил в толпе два горящие, стремящиеся к нему взгляда изнуренной, на вид чахоточной, Хотя и молодой еще крестьянки. Она глядела молча, глаза просили о чем-то, но она как бы боялась приблизиться.
— Ты с чем, родненькая?
— Разреши мою душу, родимый, — тихо и не спеша промолвила она, стала на колени и поклонилась ему в ноги.
— Согрешила, отец родной, греха моего боюсь.
Старец сел на нижнюю ступеньку, женщина приблизилась к нему, не вставая с колен.
— Вдовею я, третий год, — начала она полушепотом, сама как бы вздрагивая. — Тяжело было замужем-то, старый был он, больно избил меня. Лежал он больной; думаю я, гляжу на него: а коль выздоровеет, опять встанет, что тогда? И вошла ко мне тогда эта самая мысль...
— Постой, — сказал старец и приблизил ухо свое прямо к ее губам. Женщина стала продолжать тихим шепотом, так что ничего почти нельзя было уловить. Она кончила скоро.
— Третий год? — спросил старец.
— Третий год. Сперва не думала, а теперь хворать начала, тоска пристала.
— Издалека?
— За пятьсот верст отселева.
— На исповеди говорила?
— Говорила, по два раза говорила.
— Допустили к причастию-то?
— Допустили. Боюсь; помирать боюсь.
— Ничего не бойся, и никогда не бойся, и не тоскуй. Только бы покаяние не оскудевало в тебе — и всё бог простит. Да и греха такого нет и не может быть на всей земле, какого бы не простил господь воистину кающемуся. Да и совершить не может совсем такого греха великого человек, который бы истощил бесконечную божью любовь. Али может быть такой грех, чтобы превысил божью любовь? О покаянии лишь заботься, непрестанном, а боязнь отгони вовсе. Веруй, что бог тебя любит так, как ты и не помышляешь о том, хотя бы со грехом твоим и во грехе твоем любит. А об одном кающемся больше радости в небе, чем о десяти праведных, сказано давно. Иди же и не бойся. На людей не огорчайся, за обиды не сердись. Покойнику в сердце всё прости, чем тебя оскорбил, примирись с ним воистину. Коли каешься, так и любишь. А будешь любить, то ты уже божья... Любовью всё покупается, всё спасается. Уж коли я, такой же, как и ты, человек грешный, над тобой умилился и пожалел тебя, кольми паче бог. Любовь такое бесценное сокровище, что на нее весь мир купить можешь, и не только свои, но и чужие грехи еще выкупишь. Ступай и не бойся.
Он перекрестил ее три раза, снял с своей шеи и надел на нее образок. Она молча поклонилась ему до земли. Он привстал и весело поглядел на одну здоровую бабу с грудным ребеночком на руках.
— Из Вышегорья, милый.
— Шесть верст, однако, отсюда, с ребеночком томилась. Чего тебе?
— На тебя глянуть пришла. Я ведь у тебя бывала, аль забыл? Не велика же в тебе память, коли уж меня забыл. Сказали у нас, что ты хворый, думаю, что ж, я пойду его сама повидаю: вот и вижу тебя, да какой же ты хворый? Еще двадцать лет проживешь, право, бог с тобою! Да и мало ли за тебя молебщиков, тебе ль хворать?
— Спасибо тебе за всё, милая.
— Кстати будет просьбица моя невеликая: вот тут шестьдесят копеек, отдай ты их, милый, такой, какая меня бедней. Пошла я сюда, да и думаю: лучше уж чрез него подам, уж он знает, которой отдать.
— Спасибо, милая, спасибо, добрая. Люблю тебя. Непременно исполню. Девочка на руках-то?
— Девочка, свет, Лизавета.
— Благослови господь вас обеих, и тебя и младенца Лизавету. Развеселила ты мое сердце, мать. Прощайте, милые, прощайте, дорогие, любезные.
Он всех благословил и глубоко всем поклонился.
о тексте/оглавление	

'''
strin.replace(',', ' ')
strin.replace('-', ' ')
strin.replace('\'', ' ')
strin.replace('\"', ' ')



listoken = nltk.word_tokenize(strin)
listsent = strin.split('.')
print(len(listoken)/len(listsent))
sum=0
for i in listsent:
    sum+=len(i)
print(sum/len(listsent))