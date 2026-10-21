# 국내 치과산업 데이터 플랫폼: 기업·의료기기·무역·특허·R&D·투자·임상 (조사 시점 2026-10)

**조사 방법상의 한계 (보고서 작성자 필독)**
- 이 세션에서는 WebFetch와 curl로 외부 사이트(data.go.kr, udiportal.mfds.go.kr, newsis.com 등)에 직접 접속할 수 없었다. 프록시가 403으로 거부했고 DNS도 실패했다. 모든 근거는 WebSearch 결과(검색엔진이 반환한 URL과 요약)에 한정된다.
- "URL 확인"은 검색 결과에 해당 URL이 실제로 노출되었다는 뜻이다. 직접 접속해 메뉴를 확인한 것은 아니다. 검색 결과에 노출되지 않은 URL은 '미확인'으로 표시했다.
- 검색 결과 요약문은 도구가 생성한 2차 요약이다. 수치와 메뉴 경로는 원문 대조를 권장한다.
- 조사자의 사전 지식으로 알려진 도메인(emedi.mfds.go.kr 외 일부)이라도 검색에서 서비스 내용이 확인되지 않으면 '미확인'으로 처리했다.

---

## 1. 식약처 의료기기 허가·신고·심사 정보 (치과용 임플란트·레진 등 품목 허가 현황 조회)

### Takeaway
식약처는 현재 "의료기기정보포털(udiportal.mfds.go.kr)" 도메인 아래에 허가 DB 검색(생활 속 의료기기 > 의료기기 DataBase 검색), 전자민원, UDI추적관리시스템을 모두 운영한다. 허가 정보의 프로그램 접근은 공공데이터포털 'OpenAPI 의료기기 품목허가 정보'로 가능하다. 치과 품목만 따로 모은 공식 대시보드는 확인하지 못했고, 품목명(예: 치과용임플란트고정체)이나 업체명으로 검색해서 쓰는 구조다.

### Cited Findings
- 의료기기정보포털은 식약처 운영의 대한민국 공식 의료기기정보포털이다. 도메인 udiportal.mfds.go.kr 아래에 정책(공급내역 보고 등), 생활 속 의료기기, 사이트맵, 전자민원(msismext/emd), UDI추적관리(msismext/udi) 페이지가 확인된다 — [의료기기정책 > 공급내역 보고](https://udiportal.mfds.go.kr/contents/MNU10025), [사이트맵](https://udiportal.mfds.go.kr/sitemap/P99_05), [UDI추적관리시스템 메인](http://udiportal.mfds.go.kr/msismext/udi/min/mainView.do), [의료기기전자민원시스템](http://udiportal.mfds.go.kr/msismext/emd/min/mainView.do)
- "생활 속 의료기기 > 의료기기 DataBase 검색" 화면이 있고, UDI-DI 코드, 코드체계, 제조/수입 여부, 업체명, 모델명, 제품명, 취소·취하 여부, 추적관리대상 여부, 멸균 방법, 사용목적, 요양급여 정보 등을 제공한다고 검색 요약에 나온다 — [의료기기 DataBase 검색](https://udiportal.mfds.go.kr/search/data/P02_01) (페이지 자체의 필드 목록은 직접 확인하지 못했고 검색 요약 기준)
- 전자민원창구와 UDI추적시스템은 아이디는 동일해도 비밀번호가 다른 별도 계정일 수 있다는 안내가 있다. 즉 허가 DB 검색은 로그인 없이, 제출·신고 업무는 업체 계정으로 이용하는 구조다 — [UDI추적관리시스템 메인](http://udiportal.mfds.go.kr/msismext/udi/min/mainView.do) (검색 요약 기준)
- "제품정보방 > 광고사전심의정보" 화면이 같은 도메인에 있다 — [광고사전심의정보](http://udiportal.mfds.go.kr/msismext/emd/ifm/adPreDlbrInfoView.do)
- 과거 보도에 따르면 의료기기 정보포털은 식약처 허가 DB를 누구나 검색할 수 있고, PC와 스마트폰에서 모두 이용 가능하며, 제품의 UDI 코드를 스캔해 허가정보를 확인하는 모바일 기능을 제공한다고 소개됐다(2016~2018년 기사이므로 현행 기능과 다를 수 있음) — [메디칼타임즈](https://www.medicaltimes.com/Main/view.html?ID=1109477)
- emedi.mfds.go.kr은 검색에서 "의료기기 제조(수입)업 허가증 진위확인" 페이지(영문)로 노출됐다. 증명서 발급 업무가 민원24에서 식약처로 이전됐다는 설명이 함께 있다. 허가 DB 검색용 사이트로 확인되지는 않았다 — [허가증 진위확인(영문)](https://emedi.mfds.go.kr/msismext/emd/uif/issuDocTruflsEngView.do)
- 공공데이터포털에 식약처의 '의료기기 품목허가 정보' OpenAPI가 있다. 제공 항목은 품목명, 품목등급, 품목허가번호, 허가일자, 품목상태, 업체명 등이며 형식은 JSON/XML, 이용허락범위 제한 없음, 갱신주기 실시간으로 표시된다. 이용하려면 공공데이터포털 회원가입 후 활용신청으로 인증키를 받는 방식이 일반적이다 — [data.go.kr 15057456](https://www.data.go.kr/catalog/15057456/openapi.json) (검색 결과에 노출된 URL. 상세 페이지 data.go.kr/data/15057456/openapi.do는 직접 열람 못 함)
- 식약처 UDI-DI 제품정보를 전용으로 제공하는 data.go.kr OpenAPI는 이번 검색에서 확인되지 않았다 — 검색 결과에 해당 API 없음 (data.go.kr/data/15087442, 15090589 페이지가 노출됐으나 무엇인지 확인 불가)

### Inferences
- 치과 품목 허가 현황은 "품목명 검색(치과용임플란트고정체, 치과용레진 등) 또는 OpenAPI 전체 다운로드 후 품목명 필터"로 직접 구성해야 한다. 공식 '치과 전용' 현황판은 확인되지 않았다.
- 과거 이름이던 emed.mfds.go.kr(의료기기 정보마당)과 emed.kfda.go.kr은 현재 udiportal 도메인으로 통합된 것으로 보인다(다만 통합·종료를 명시한 공지는 찾지 못했다).

### Gaps
- emedi.mfds.go.kr의 현재 허가 조회 메뉴 구성은 확인하지 못했다.
- OpenAPI의 정확한 오퍼레이션 목록, 일일 호출 한도, 치과용 품목 분류코드(품목 분류번호) 체계는 확인하지 못했다.
- 의약품안전나라(nedrug.mfds.go.kr)에서 의료기기를 다루는지는 이번 조사에서 확인되지 않았다(미확인).

---

## 2. UDI(의료기기 통합정보센터), 생산·수입·수출 실적 통계, 건강보험 치료재료 정보

### Takeaway
식약처가 매년 5월경 '국내 의료기기 생산·수출·수입 실적' 보도자료를 낸다. 2025년 실적에서 치과용 임플란트 고정체는 생산 1위, 수출 2위 품목이다. UDI 공급내역 보고는 의료기관에 공급되는 3·4등급 이식형 기기와 요양급여 치료재료가 대상이라 임플란트 공급 흐름 분석에 유용하나, 공급내역의 통계 공개 여부는 확인하지 못했다. 치료재료는 심평원(HIRA)이 관리하며 치과용 재료는 L군(일반재료군 Ⅱ)에 포함된다.

### Cited Findings
- 식약처 2025년 실적(2026-05-28 발표): 생산액 12조 3,558억원(전년 대비 +8.1%), 수출액 7조 6,395억원(53.7억 달러, +2.2%), 수입액 7조 1,606억원(50.4억 달러, +9.3%), 무역수지 4,789억원 흑자(6년 연속), 국내 시장 11조 8,769억원(+12.6%) — [Finance Scope](https://www.finance-scope.com/article/view/scp202605280012), [Newsis](https://www.newsis.com/view/NISX20260528_0003646894), [메디파뉴스](https://medifonews.com/news/article.html?no=213914)
- 치과용임플란트고정체: 2025년 생산액 2조 4,429억원(+12.2%)으로 3년 연속 생산 1위, 수출은 3.99억 달러로 2위(1위는 범용초음파영상진단장치 5.29억 달러). 이 수치는 검색 요약 1건에서 나온 것으로 원문 대조가 필요하다 — [Newsis](https://www.newsis.com/view/NISX20260528_0003646894), [메디파뉴스](https://medifonews.com/news/article.html?no=213914). 다른 검색 요약에서는 임플란트 고정체 세부 금액이 확인되지 않았다는 응답도 있었다(수치 일관성 미검증)
- 2024년 실적(2025년 5월 발표): 치과용 임플란트가 생산·수출 모두 2년 연속 1위였다 — [Kukinews](https://www.kukinews.com/article/view/kuk202405280123) 등 검색 결과 (요약 기준)
- 과거 비교: 2016년 임플란트 수출 2,296억원(2.03억 달러)으로 수출 2위, 2011년 임플란트 생산 2,497억원 — [Medigate](https://www.medigatenews.com/news/2011620906) 등 (요약 기준)
- UDI 공급내역 보고: 제조·수입·판매·임대업자가 의료기관 등에 공급할 때 의료기기통합정보시스템으로 보고하며 공급한 달의 다음 달 말일까지 제출한다. 2026년 보고 기한 공지(2026-04-14)도 게시돼 있다 — [공급내역 보고](https://udiportal.mfds.go.kr/contents/MNU10025)
- 공급내역 보고 대상은 3·4등급 인체이식형 의료기기와 요양급여대상 치료재료(의료기관 공급 한정)이고, 시행규칙 개정으로 공급내역 보고 서식(별지 제48호의2)에 약 20개 항목이 신설되고 금액은 부가세 포함 거래명세서 단위로 적도록 했다는 2017~2018년 보도가 있다 — [메디칼타임즈 ID=1118406](https://www.medicaltimes.com/Main/view.html?ID=1118406) (현행 제도와 차이 가능)
- 의료기기통합정보센터 콜센터 1899-9351 — [메디칼타임즈 ID=1118406](https://www.medicaltimes.com/Main/view.html?ID=1118406)
- 의료기기 DataBase 검색 화면에 '요양급여 정보' 항목이 있어 허가 정보와 급여 정보를 함께 확인할 수 있다 — [의료기기 DataBase 검색](https://udiportal.mfds.go.kr/search/data/P02_01) (요약 기준)
- 심평원 공개 PDF에 치료재료 군 분류가 정리돼 있다: K군(일반재료군 Ⅰ), L군(일반재료군 Ⅱ: 장루용·혈액투석용·치과용재료 등), M군(일반재료군 Ⅲ), N군(정액수가), P군(한방재료), S군(선별급여) — [HIRA PDF](https://www.hira.or.kr/bbs/68/2024/07/BZ202407290304584.pdf) (요약 기준)
- 치과 재료대 신고는 급여목록·급여상한금액표에 등재된 치과재료만 대상이며, 비급여·정액보상·전액본인부담 품목은 신고 대상이 아니다 — [치과신문 건강보험 가이드북](https://www.dentalnews.or.kr/mobile/article.html?no=32688) (2022년 자료)
- 치과 임플란트 건강보험은 국민건강보험공단에서 안내하며 요양기관정보마당에서 임플란트 대상자 자격조회를 한다 — [NHIS 치과임플란트 급여안내](https://www.nhis.or.kr/static/html/wbma/c/wbmac0221.html)
- 식약처 의료기기 산업 분석 보고서(연간 실적 책자) 원문 PDF의 URL은 검색에서 확인하지 못했다(미확인)

### Inferences
- 식약처 연간 실적 보도자료는 "품목별 생산·수출·수입 상위 순위"를 담고 있어 임플란트 고정체의 시계열(연도별 생산·수출액)을 쌓기에 가장 쉬운 공식 출처다. 치과용 레진·보철 등 하위 품목은 상위 순위에 안 잡히므로 보고서 부록 표(미확인)가 필요할 수 있다.
- UDI 공급내역은 급여 치료재료(임플란트 포함)의 의료기관별 공급량을 포착하나 공개 통계 형태가 확인되지 않아, 제3자가 자유롭게 쓰기는 어려울 가능성이 높다.

### Gaps
- UDI 공급내역 집계 통계의 공개 여부와 한국의료기기안전정보원(KMDSIA)의 별도 통계 서비스 URL은 확인하지 못했다.
- HIRA 치료재료 급여·비급여 목록 조회 페이지의 정확한 URL과 치과 대분류 코드는 확인하지 못했다. 코드 체계는 군 분류(L군 등)까지만 확인.
- 한국의료기기산업협회(KMDIA) 및 의료기기산업 종합정보시스템의 직접 자료는 검색에서 확인되지 않았다(미확인).

---

## 3. 무역통계 (HS 9018.4x, 9021.29, 3006.40 등)

### Takeaway
국내 접근 가능한 무역통계는 관세청 수출입무역통계, 한국무역협회 K-stat(stat.kita.net), 공공데이터포털 관세청 OpenAPI 3축이다. K-stat은 HSK 2/4/6/10단위 조회를 지원하는 것으로 보이고 원자료는 관세청이다. 치과 품목은 HS 9018.41(치과용 드릴 엔진), 9018.49(기타 치과용), 9021.29(치과용 보철류), 3006.40(치과용 시멘트 등)을 10단위 HSK로 내려가 조회한다.

### Cited Findings
- K-stat(stat.kita.net)은 보통무역통계(수출입신고 물품 집계)이며, 품목별 조회는 '국내통계 > 한국무역 > 품목 수출입'에서 HSK/MTI/SITC 코드 기준으로 한다. 수출은 FOB, 수입은 CIF 기준이라 다른 기관 수치와 차이가 날 수 있다 — [K-stat 통계가이드](https://stat.kita.net/stat/guide/guide_19.screen)
- K-stat 품목 수출입 화면에는 HSK 2/4/6/10단위 조회 옵션이 있는 것으로 보이며 출처는 관세청이다 — [품목 수출입](https://stat.kita.net/stat/kts/pum/ItemImpExpList.screen), [품목코드](https://stat.kita.net/stat/kts/statCode/ItemHierCodeList.screen) (검색 요약 기준)
- 공공데이터포털에 관세청 '품목별 국가별 수출입실적' OpenAPI가 있다. 서비스키, 시작·종료 년월, 국가코드가 필수이고 품목코드는 선택, 조회기간은 1년 이내다 — [data.go.kr 15100475](https://www.data.go.kr/en/data/15100475/openapi.do)
- 관세청 '시도별 품목별 수출입무역통계'(HSCode 기준) 데이터가 공공데이터포털에 있다 — [data.go.kr 15101641](https://www.data.go.kr/catalog/15101641/openapi.json)
- HSK 2·4·6·10단위 표준품명·성질별 분류표(XLSX)가 공공데이터포털에 있다 — [data.go.kr 15049720](https://www.data.go.kr/catalog/15049720/fileData.json)
- 관세청은 시·군·구 단위 세부 자료를 과세정보로 보고 비공개해 왔고 유관기관에도 세부 통계 비공개를 요청했다는 기사가 있다(기사 시점 미확인) — [스마트투데이](https://www.smarttoday.co.kr/ko-kr/articles/111033)
- KOTRA 트라이빅(TriBIG)의 '한국무역현황 상세통계' 데이터셋이 HS 10자리까지 지원한다는 설명이 data.go.kr에 있다 — [data.go.kr 15140428](https://www.data.go.kr/catalog/15140428/fileData.json) (요약 기준)
- HS 9018.41은 치과용 드릴 엔진(다른 치과용 장비와 단일 베이스에 결합된 것 포함)이다. 한국 10단위 9018419000(부분품·부속품)의 MFN 세율이 8%라는 제3자 사이트 정보가 있으나 관세청 확인이 필요하다 — [Flexport HS](https://www.flexport.com/data/hs-code/901841-dental-drill-engines-whether-or-not-combined-on-a-single-base-with-other-dental-equipment-and-parts-and-accessories-thereof/), [Treayo](https://treayo.com/en/hs/korea/90184190)
- 관세청 UNI-PASS는 2025년경 전산 전면 교체(총 1,060억원)를 거쳐 신형 시스템을 가동했다고 보도됐다. 무역통계 조회 서비스(tradedata.go.kr)의 개편 여부는 확인되지 않았다 — [티에프미디어](https://tfmedia.co.kr/mobile/article.html?no=185582)
- 관세청 UNI-PASS 무역통계(unipass.customs.go.kr)와 tradedata.go.kr의 실제 페이지는 검색 결과에 노출되지 않아 URL은 미확인이다. ITC Trade Map, KOTRA 해외시장뉴스 등도 이번 검색 범위에서 확인하지 못했다(미확인)

### Inferences
- 치과 분석은 HSK 10단위 코드 목록(9018.41, 9018.49, 9021.29, 3006.40, 임플란트는 9021.29 하위 등 국내 세번 확인 필요)을 K-stat이나 관세청 API로 시계열화하는 방식이 현실적이다. 임플란트 고정체의 정확한 HSK 10단위 코드는 이번 조사에서 확인하지 못했으므로 분석 전에 관세청 HSK 표로 검증해야 한다.
- K-stat 수치와 관세청 수치, 식약처 수출입 실적은 집계 기준(FOB/CIF, 품목 분류)이 달라 서로 맞지 않을 수 있다.

### Gaps
- tradedata.go.kr 및 UNI-PASS 무역통계의 현재 메뉴, 접근 조건(회원가입 여부)은 확인하지 못했다.
- K-stat 로그인 필요 여부, 다운로드 한도, 유료 구간 여부는 확인하지 못했다.
- ITC Trade Map 등 국제 무역 DB의 국내 접근 조건은 조사하지 못했다.

---

## 4. 특허·R&D (KIPRIS, NTIS, 범부처 의료기기 R&D, 치의학 연구기관)

### Takeaway
특허는 KIPRIS(무료 검색)와 KIPRIS Plus(OpenAPI·대량 데이터)로, 정부 R&D는 NTIS(KISTI 운영)로, 의료기기 전주기 R&D는 범부처전주기의료기기연구개발사업단(2026년부터 후속 '범부처 첨단 의료기기 R&D')의 공고·성과로 확인한다. 한국치의학연구원은 설립 근거를 찾지 못했고 국립치의학연구원 유치전(부산·대구)만 확인된다.

### Cited Findings
- KIPRIS는 한국특허정보원이 특허청과 함께 운영하는 무료 특허정보 검색 서비스로, 국내 특허·실용신안·디자인·상표와 미국·유럽·일본·중국·WIPO 등 해외 정보를 제공한다. 2025년 2월 전면 개편을 거쳤다는 블로그 설명이 있다(블로그 출처이므로 공식 확인 필요) — [KIPRIS 가이드(limeade)](https://limeade.kr/%ED%8A%B9%ED%97%88%EC%A0%95%EB%B3%B4%EA%B2%80%EC%83%89%EC%84%9C%EB%B9%84%EC%8A%A4-kipris%ED%82%A4%ED%94%84%EB%A6%AC%EC%8A%A4-%EC%99%84%EB%B2%BD-%EA%B0%80%EC%9D%B4%EB%93%9C/)
- KIPRIS Plus(plus.kipris.or.kr)는 2024년 보도 기준 13개국 산업재산권 공보와 특허 행정정보 등 총 120종 데이터 상품을 파일 또는 OpenAPI로 개방한다. 2024년 5월 한·미·일 특허 권리자 변동정보 약 2,800만건이 추가됐다 — [데일리팜](https://dailypharm.com/user/news/31375)
- 공공데이터포털 KIPRIS 계열 API 한 종은 월 1,000회까지 무료 호출이고 그 이상이나 BULK는 plus.kipris.or.kr에서 이용하도록 안내한다(해당 API 한정 조건) — [data.go.kr 15039347](https://www.data.go.kr/data/15039347/openapi.do)
- KIPRIS Plus API는 ServiceKey 파라미터를 쓰고 키워드 검색(getWordSearch), 출원번호 기준 서지상세(getBibliographyDetailInfoSearch) 등의 오퍼레이션이 있다는 제3자 문서가 있다 — [k-skill korean-patent-search](https://skillselion.com/skills/nomadamas/k-skill/korean-patent-search) (비공식)
- NTIS(ntis.go.kr)는 KISTI가 운영하는 국가연구개발 사업·과제·인력·장비·성과 지식포털이다. 2017년 개편으로 공개 항목이 295개로 확대되고 회원가입 시 누구나 검색결과를 다운로드할 수 있게 됐다는 보도가 있다(2017년 기준) — [아주경제 2017](https://www.ajunews.com/view/20170413104445365)
- NTIS 오픈API 공식 정책(신청·키·호출 제한)은 확인하지 못했다. 제3자 MCP 래퍼가 있으나 비공식이다 — [glama ntis-mcp](https://glama.ai/mcp/servers/vertical-mcp/ntis-mcp)
- 범부처전주기의료기기연구개발사업단은 과기부·산업부·복지부·식약처 4개 부처가 2020~2025년 약 1.2조원을 지원했고, 467개 과제와 1,443개 기관 참여, 169건 인허가 성과가 보도됐다. 2026년부터 '범부처 첨단 의료기기 연구개발사업'으로 2026~2032년 7년간 약 9,400억원 규모로 이어진다(예정) — [데일리팜 6년 성적표](https://dailypharm.com/user/news/334193), [데일리팜 169건 인허가](https://dailypharm.com/user/news/334178)
- THE VC에 사업단(KMDF) 페이지가 있다 — [THE VC KMDF](https://thevc.kr/kmdf). 사업단 공식 홈페이지 URL은 확인하지 못했다(미확인)
- 한국치의학연구원: 설립·개원을 확인하는 자료는 없었다. 부산시가 '국립치의학연구원' 유치 추진위원회를 2024-11 발족하고 2025-11 5차 실무 TF를 운영했으며, 대구·경북도 치과기기 생산 65%·수출 80% 이상을 근거로 유치를 주장한다 — [부산시 K-dental](https://www.busan.go.kr/k-dental/news/1655285), [부산시 TF](https://www.busan.go.kr/k-dental/news/1706845), [경북매일](https://www.kbmaeil.com/article/20250728500003)

### Inferences
- 치과 특허 분석은 KIPRIS의 IPC(예: A61C 치과, A61K 6 치과용 조제) 필터로 출원인(오스템·덴티움·디오 등)별 집계가 가능하다고 판단되나, 이 IPC 필터 기능 자체는 이번 조사에서 확인하지 못했다.
- 치과 R&D 과제는 NTIS 키워드/분류 검색으로 추출해야 한다. 사업단 과제 중 치과 전용 사업은 이번에 확인되지 않았다.

### Gaps
- KIPRIS Plus의 요금·무료 한도(전체)와 NTIS 오픈API 신청 방법은 확인하지 못했다.
- 한국치의학연구원이라는 실존 기관은 확인되지 않았다(국립치의학연구원은 유치 단계). 한국보건산업진흥원(KHIDI)의 치과 관련 사업은 이번에 확인하지 못했다.

---

## 5. 기업정보·투자 (DART, KRX, 신용평가·기업정보 서비스, 스타트업 DB)

### Takeaway
상장 치과기업의 공시·재무는 DART/OpenDART가 1차 출처이고, KRX 정보데이터시스템·공공데이터포털 'KRX상장종목정보'로 종목 목록을 보완한다. 스타트업·투자 정보는 THE VC와 혁신의숲이 검색에서 확인됐으며 상세 정보는 유료·회원가입 구간이 있다. NICE기업정보·크레탑 등은 이번 조사에서 확인하지 못했다.

### Cited Findings
- OpenDART: 종목코드(stock_code)와 별개의 8자리 고유번호(corp_code)를 corpCode.xml(ZIP)로 받아 조회한다. 단일회사 전체 재무제표는 fnlttSinglAcntAll.json이고 사업연도는 2015년 이후만 조회 가능하다 — [AlgoLab 블로그](https://algolab.co.kr/blog/dart-opendart-financial-statement-api-lag-2026), [wikidocs](https://wikidocs.net/336171)
- OpenDART 일일 호출 한도는 출처가 엇갈린다: 일 20,000건(AlgoLab) vs 일 10,000건(MCP 서버 문서). 공식 가이드 미확인 — [AlgoLab 블로그](https://algolab.co.kr/blog/dart-opendart-financial-statement-api-lag-2026); 상충: [OpenDART MCP Server](https://mcpservers.org/ja/servers/songhyojun0228/opendart-mcp-server)
- dart.fss.or.kr, opendart.fss.or.kr 공식 페이지는 검색 결과에 노출되지 않았다. 오스템임플란트·덴티움·디오·바텍·레이·하이니스·아이덴티의 공시 페이지 URL도 확인하지 못했다(미확인)
- 덴티움 매출 중 임플란트 83%, 중국 50%라는 증권사 분석이 있으나 연도 불명이다 — [dealsite](https://dealsite.co.kr/articles/123345) (연도 미확인으로 사용 주의)
- 공공데이터포털 'KRX상장종목정보'는 기준일자, 단축코드, ISIN, 시장구분, 종목명, 법인등록번호, 법인명을 일 1회 갱신하며 업종 항목은 없다 — [data.go.kr 15094775](https://www.data.go.kr/data/15094775/openapi.do)
- KRX 정보데이터시스템(data.krx.co.kr)은 검색에서 확인되지 않았다(미확인). KRX 헬스케어 지수가 2026년 9월 정기변경에서 67개에서 48개 종목으로 축소됐다는 보도가 있다 — [메디칼타임즈](https://www.medicaltimes.com/Users/News/NewsView.html?ID=1170672)
- THE VC: 스타트업 투자 DB로 '치과기업' 컬렉션(8개사)이 있고 라운드·투자자·최근 투자 정보가 보인다. 투자자명·재무제표 등 상당 부분은 Pro 플랜에서만 열린다 — [THE VC 치과 컬렉션](https://thevc.kr/collections/65f449c981a1b40a1547efa3), [Arcreal](https://thevc.kr/arcreal), [Dencomm](https://thevc.kr/dencomm), [Dentronic](https://thevc.kr/dentronic)
- 예시: 아크리얼(Arcreal)은 2021년 5월 설립, 시드 61억원 유치(구강스캐너·덴탈 플랫폼), 덴컴(Dencomm)은 Series A, 덴트로닉은 사우스파크커먼스 프리시드 약 100만 달러 — [THE VC Arcreal](https://thevc.kr/arcreal), [THE VC Dentronic](https://thevc.kr/dentronic) (요약 기준)
- 혁신의숲(innoforest.co.kr): 마크앤컴퍼니의 스타트업 성장 분석 플랫폼(2021 출시)으로 트래픽·소비자거래·고용·재무·투자 데이터를 최근 3개년 월간 갱신으로 제공한다. 2021년 말 4,000여개 스타트업 데이터를 무료 개방했으나 현재 요금·무료 범위는 확인되지 않았고 최근 리포트는 무료 회원가입을 요구한다 — [혁신의숲 3주년 리포트](https://www.innoforest.co.kr/report/NS00000319), [혁신의숲 2주년](https://www.innoforest.co.kr/report/NS00000212)
- 벤처스퀘어는 치과 스타트업 기사가 노출됐으나 DB 서비스 여부는 확인하지 못했다 — [벤처스퀘어](https://www.venturesquare.net/865402/embed)
- NICE기업정보, 크레탑, 잡플래닛은 이번 검색에서 서비스 내용을 확인하지 못했다(미확인)

### Inferences
- 상장 치과기업 재무 비교는 OpenDART(corp_code 확보 후 재무제표 API)로 자동화할 수 있고, 비상장 중견기업(예: 외부감사 대상)은 DART 감사보고서가 유일한 공개 출처일 가능성이 높다.
- 스타트업 투자는 THE VC 무료 구간으로 목록·라운드 규모 정도만 보고, 투자자·재무 상세는 유료 플랜이 필요하다.

### Gaps
- 상장 치과사 종목코드, 사명 변경 이력, 상장폐지 여부는 이번에 확인하지 않았다.
- 크레탑·NICE·잡플래닛 서비스 URL, 가입·유료 조건은 미확인.

---

## 6. 임상시험·학술

### Takeaway
국내 임상연구 등록은 질병관리청 국립보건연구원의 CRIS(WHO 1차 등록기관), 의료기기 임상시험 승인 정보는 식약처 보도자료·통계로 확인된다. 치과 전용 임상 DB는 확인되지 않았다.

### Cited Findings
- CRIS(Clinical Research Information Service)는 국립보건연구원(질병관리청 소속)이 운영하며 2010년 WHO 1차 레지스트리로 가입했고 등록 정보가 WHO ICTRP로 전송된다. WHO 등록소 페이지에 안내된 주소는 cris.nih.go.kr 계열, 문의는 criskorea@korea.kr — [WHO CRiS 페이지](https://www.who.int/clinical-trials-registry-platform/network/primary-registries/republic-of-korea-clinical-research-information-service-(cris))
- 2017년 기준 CRIS 등록 임상연구는 2,350건으로 전체 중 일부라는 지적이 있다. 현재 건수는 확인되지 않았다 — [메디게이트 2017](https://medigatenews.com/news/3483246463)
- 임상연구 요양급여 결정신청서에 CRIS 등록번호를 적도록 돼 있다 — [한림대 첨부 PDF](https://research.hallym.or.kr/chpfile/humcctc/첨부2. 임상연구의 요양급여 적용에 관한 안내_홈페이지용.pdf) (요약 기준)
- K-CLIC: 임상시험 정보를 모은 포털사이트로 2017년 보도됐다. 현재 운영 여부는 미확인 — [데일리팜](https://m.dailypharm.com/user/news/88037)
- 식약처 의료기기 임상시험계획 승인 통계는 보도자료로 나온다. 예: 2017년 승인 84건(기구·기계류 43, 의료용품류 25, 체외진단용 16). 최근 연도 기사에는 등급별 건수(4등급 12, 3등급 28, 2등급 23)가 있으나 기준 연도가 불명확하다 — [경향 스포츠 2018](https://sports.khan.co.kr/article/201804171616013), [코메디](https://kormedi.com/1214019/)
- 식약처 nedrug 임상시험 검색 페이지는 검색에서 확인되지 않았다(미확인)

### Inferences
- 치과 임플란트·치과용 레진 임상은 보통 비교적 낮은 등급(2~3등급)이라 임상시험 자체가 적을 가능성이 있다. 이 추론은 위 자료에서 직접 입증되지 않았다.

### Gaps
- CRIS 공식 페이지의 현재 검색·다운로드 기능, 식약처 임상시험 정보 포털의 현재 URL, 치과 관련 임상 건수는 확인하지 못했다.
- 대한치과의사협회, 치의학 학회 데이터베이스(KoreaMed, KCI 등)는 이번 조사에서 다루지 못했다.

---

## 7. 글로벌 보조 데이터 소스 (간략)

### Takeaway
WHO와 FDI가 구강보건 국가 비교 데이터를 제공한다. OECD 구강 통계는 확인하지 못했다.

### Cited Findings
- WHO Global Health Observatory의 구강보건 데이터 포털은 Global oral health status report 국가 프로파일 기반이다(GBD, IARC, WHO 조사 데이터). 2019년 전 세계 약 35억명이 구강질환을 겪는다고 제시 — [WHO GHO 구강보건 포털](https://www.who.int/data/gho/data/themes/oral-health-data-portal), [WPRO 국가 프로파일](https://data.wpro.who.int/oral-health-country-profiles-2022/)
- FDI Data Hub for Global Oral Health(2014 출범)는 WHO, 니가타대, 말뫼대, 세계은행, Globocan 데이터를 지표·국가·연도별 지도·표로 제공하고 다운로드가 가능하다. 2009년 Oral Health Atlas를 계승했다 — [OASIS 소개](https://oasisdiscussions.ca/2014/10/02/dhgoh/), [FDI Oral Health Observatory](https://www.fdiworldental.org/10-years-oral-health-observatory-data)
- OECD Health Statistics의 구강 관련 지표는 검색 결과에서 확인되지 않았다(미확인)

### Inferences
- 한국 치과 소비·서비스 수준의 국제 비교는 WHO/FDI의 질병부담 데이터가 중심이며 시장 규모 비교용 데이터는 별도 유료 리서치(예: GII Korea 보고서)에 의존해야 한다. GII Korea 등은 유료 시장보고서 판매 사이트로 확인된다 — [GII Korea 치과기기](https://m.giikorea.co.kr/topics/MC06_kr.html)

### Gaps
- OECD Health Statistics의 구강 지표 접근 방법은 미조사. 해외 접근 조건(회원/유료)은 확인하지 못했다.

---

## 플랫폼 요약표 (보고서 작성자용)

| 플랫폼 | 운영기관 | URL 확인 상태 | 데이터 | 형태 | 비용/접근 | 치과 활용 포인트 |
|---|---|---|---|---|---|---|
| 의료기기정보포털 | 식약처 | udiportal.mfds.go.kr 확인(검색 노출) | 허가 DB, UDI-DI, 급여정보 | 웹 검색 | 무료(검색), 업체는 계정 | 품목·업체별 허가 현황 |
| 의료기기 품목허가 정보 API | 식약처(공공데이터포털) | data.go.kr/catalog/15057456 확인 | 품목명, 등급, 허가번호, 일자, 상태, 업체 | OpenAPI(JSON/XML) | 무료, 활용신청 | 치과 품목 필터 시계열 |
| 연간 생산·수출·수입 실적 | 식약처 | 보도 기사로만 확인, 원문 미확인 | 품목별 순위·금액 | 보도자료/보고서 | 무료 | 임플란트 고정체 생산·수출 추세 |
| UDI 공급내역 보고 | 식약처/통합정보센터 | udiportal 공지 확인 | 3·4등급 이식형, 급여 치료재료 공급 | 보고 시스템(제출용) | 업체 한정 | 통계 공개 여부 미확인 |
| 치료재료 급여목록 | 심평원 | hira.or.kr 일부 PDF 확인, 조회 페이지 미확인 | 군별 치료재료(L군에 치과재료) | 목록 파일 | 무료 | 급여 등재 임플란트·재료 |
| K-stat | 한국무역협회 | stat.kita.net 확인 | HSK 품목별 수출입 | 웹 조회 | 무료 여부 미확인 | 치과 HS코드 수출입 |
| 관세청 수출입무역통계 | 관세청 | URL 미확인(OpenAPI는 data.go.kr 확인) | 품목·국가별 | 웹/API | OpenAPI 무료(키) | 원자료 |
| KIPRIS / KIPRIS Plus | 한국특허정보원/특허청 | kipris.or.kr, plus.kipris.or.kr 확인(검색 언급) | 특허·상표·디자인 | 검색/API/벌크 | 검색 무료, API 일부 한도 | 출원인별 치과 특허 |
| NTIS | KISTI | ntis.go.kr 확인(검색 언급) | R&D 과제·성과 | 검색/다운로드 | 회원가입 후 | 치과 R&D 과제 |
| 범부처 의료기기 R&D | 사업단 | 공식 URL 미확인 | 과제·공고·성과 | 공고 | 무료 | 정부 지원 현황 |
| DART/OpenDART | 금융감독원 | 공식 URL 미확인(제3자 문서 다수) | 공시·재무 | 웹/API | 무료, 키 | 상장 치과사 재무 |
| THE VC | 더브이씨 | thevc.kr 확인 | 투자 라운드 | 웹 | 일부 Pro 유료 | 치과 스타트업 투자 |
| 혁신의숲 | 마크앤컴퍼니 | innoforest.co.kr 확인 | 스타트업 성장 데이터 | 웹 | 회원가입(요금 미확인) | 비상장 스타트업 |
| CRIS | 국립보건연구원 | cris.nih.go.kr 계열(WHO 페이지) | 임상연구 등록 | 웹 | 무료 | 치과 임상 등록 검색 |
