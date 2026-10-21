# 국내(대한민국) 치과산업 관련 공공 데이터·통계 플랫폼 조사

> 조사 기준일: 2026-10-21. 방법상 한계: 이 세션의 네트워크 정책이 .kr 공공기관 호스트(예: opendata.hira.or.kr)에 대한 직접 접속(WebFetch/curl)을 차단했다. 그래서 모든 URL은 "웹 검색 결과로 노출된 실제 URL"이고, 페이지 본문을 직접 열람해 확인한 것은 아니다. 세부 내용은 검색 결과 요약과 KOSIS MCP 도구(통계표 ID, 수록주기)에 근거한다. 확인하지 못한 항목은 '미확인'으로 표시했다.
> KOSIS MCP 이용 고지: 본 노트의 KOSIS 통계표 정보는 국가통계포털(KOSIS) 기반 시범서비스 도구로 조회했다. 생성형 AI 특성상 오류가 있을 수 있고, 국가데이터처의 공식 입장이 아니라 참고용이다.

## 1. 건강보험심사평가원(HIRA): 보건의료빅데이터개방시스템, 요양기관 현황, 진료행위 통계, 병원정보서비스

### Takeaway
HIRA는 치과 요양기관 수와 시설·장비, 의료인력(치과의사·치과위생사 포함), 진료행위(스케일링·임플란트 등) 통계를 자체 개방시스템(opendata.hira.or.kr)과 공공데이터포털 파일/API, KOSIS로 나눠 제공한다. 개별 병원 단위 정보는 '병원정보서비스' OpenAPI(무료, 회원가입·활용신청)로 얻는다.

### Cited Findings
- 운영기관: 건강보험심사평가원. 보건의료빅데이터개방시스템은 공공데이터(데이터셋·오픈API), 의료빅데이터분석(빅데이터센터), 의료통계분석(질병·의약품·의료기관) 서비스로 구성된다. — [opendata.hira.or.kr 서비스 소개](https://opendata.hira.or.kr/op/opb/selectHelhMedDataInfoView.do)
- 개방시스템은 2015년 개방 당시 7개 분야 18개 DB를 공개했다. — [데일리팜 2015 기사](https://m.dailypharm.com/user/news/123976)
- 요양기관 수 현황 메뉴(종별·지역별·설립구분별·의원 표시과목별 기관 수)가 있고 분기마다 갱신되며, 요양기관이 건강보험법에 따라 신고한 내용 기준이다. — [기관수현황 olapYadmStatInfoTab1](https://opendata.hira.or.kr/op/opc/olapYadmStatInfoTab1.do) (갱신주기와 표시과목 분류는 검색 결과 요약 기준이며, 치과 세부 분류는 미확인)
- 종별 요양기관수 메뉴: [olapMdclRcStatsInfoTab1 (docNo=02-001)](https://opendata.hira.or.kr/op/opc/olapMdclRcStatsInfoTab1.do?docNo=02-001)
- 시설 및 장비 현황(입원실·특수진료실, 의료장비 현황)은 지역별·종별로 조회할 수 있다. — [olapInfraEquipmentStatInfoTab3](https://opendata.hira.or.kr/op/opc/olapInfraEquipmentStatInfoTab3.do)
- 진료행위(검사/수술 등) 통계와 국민관심 진료행위 통계 메뉴가 있다. 진료 후 3년 이내 청구가 가능하므로 통계 갱신까지 약 4개월 이상 걸릴 수 있다고 안내한다. — [진료행위 통계 메뉴 예시: olapDiagBhvInfoTab4](https://opendata.hira.or.kr/op/opc/olapDiagBhvInfoTab4.do)
- 치료재료 청구 정보(통계) 메뉴가 있다. 치과 재료(임플란트 재료 등) 포함 여부는 미확인. — [olapMaterialTab1](https://opendata.hira.or.kr/op/opc/olapMaterialTab1.do)
- HIRA 보도자료 기준 2022년 치과 외래 환자는 2,424만 명(국민의 47.1%, 2018년 대비 5.9% 증가)이다. 스케일링 이용자는 1,525만 8,463명(29.7%), 충치치료는 552만 5,738명(10.7%)이다. 임플란트는 65세 이상 전 연령에서 증가했고 틀니는 감소했다. — [HIRA 보도자료](https://www.hira.or.kr/bbsDummy.do?pgmid=HIRAA020041000100&brdScnBltNo=4&brdBltNo=10925&pageIndex=1&pageIndex2=1)
- HIRA 정책동향(진료경향분석) 자료는 치과 진료인원이 2010년 164만 1천 명에서 2019년 238만 3천 명으로 45.2% 증가했다고 보고한다. 이 수치는 해당 자료의 분석 정의에 따른 것으로 위 보도자료(2022년 외래 환자 2,424만 명)와 집계 기준이 다르다. — [HIRA 정책동향 PDF(repository.hira.or.kr)](https://repository.hira.or.kr/bitstream/2019.oak/2517/2/%EC%B5%9C%EA%B7%BC%2010%EB%85%84%EA%B0%84%20%EA%B1%B4%EA%B0%95%EB%B3%B4%ED%97%98%20%EC%B9%98%EA%B3%BC%20%EC%A7%84%EB%A3%8C%20%EA%B2%BD%ED%96%A5.pdf)
- 공공데이터포털 파일: '건강보험심사평가원_보건의료빅데이터개방시스템_의료인력통계_20250331'. 요양기관 활동 의료인력을 분기·지역·종별로 제공하며 의사·치과의사와 치과위생사 등 기타 의료인력 항목이 포함된다고 설명한다. XLSX, 수정일 2025-06-13. — [data.go.kr/15066021](https://www.data.go.kr/data/15066021/fileData.do)
- 공공데이터포털 파일: '건강보험심사평가원_전국 병의원 및 약국 현황_20251231'. 요양기관 기본·세부·시설·의료장비 정보를 담는다. — [data.go.kr/15051059](https://www.data.go.kr/data/15051059/fileData.do)
- 공공데이터포털 파일: '건강보험심사평가원_의원급 표시과목별 행위 통계_20251231'. — [data.go.kr/15055563](https://www.data.go.kr/data/15055563/fileData.do) (치과 포함 여부는 미확인)
- 병원정보서비스 OpenAPI: 요양기관이 심평원에 신고한 내용 기준의 병원 정보 조회. 요양기호는 암호화 값으로 제공된다. 유형 REST, XML, 무료, 개발계정 트래픽 10,000(자동승인)이고 운영계정은 심의승인이며 회원가입·활용신청이 필요하다. 지역코드 등은 개방시스템의 코드조회 메뉴에서 확인한다. — [data.go.kr/15094093 (OpenAPI)](https://www.data.go.kr/data/15094093/openapi.do) (검색 결과의 요약이며 페이지 직접 열람은 못 함. 이 URL이 병원정보서비스 페이지인지 유사 HIRA API인지 검색 요약만으로는 완전히 확정하지 못했다)
- 병원평가정보서비스 OpenAPI도 별도로 있다. — [data.go.kr/15094089](https://www.data.go.kr/data/15094089/openapi.do)
- KOSIS에도 HIRA 제공 통계표가 있다(아래 3번 참조): 시도별 종별 요양기관 현황(DT_MIRE01), 치과 연령별 성별 진료비 심사실적(DT_LEE_46).

### Inferences
- 치과 기관 수 추이는 개방시스템 기관수현황, KOSIS DT_MIRE01, 공공데이터포털 병의원 현황 파일 중 어느 쪽으로도 확보할 수 있다. 개별 치과 단위(위치·장비·인력) 분석은 '전국 병의원 및 약국 현황' 파일이나 병원정보 API가 적합하다.
- 임플란트·스케일링·틀니 등 치과 수요 지표는 HIRA 진료행위 통계와 NHIS 행위코드별 파일(2번)이 서로 보완한다.
- 치과 시장(수요) 분석에서는 연령대별 임플란트 증가율(65~69세 59.8%)이 고령층 중심 수요 성장의 근거 지표가 된다.

### Gaps
- opendata.hira.or.kr에서 '치과'만 따로 필터링할 수 있는 메뉴 구조(표시과목 '치과' 항목, 치과 전용 진료행위 분류)는 직접 열람하지 못해 미확인.
- 갱신주기는 기관수현황(분기)만 검색 결과로 확인했고, 진료행위 통계의 정기 갱신 주기는 '약 4개월 이상 소요'라는 지연 정보만 확인했다.
- 병원정보서비스 API의 오퍼레이션별 응답 필드(치과 종별 코드 등) 미확인.
- HIRA 개폐업 전용 통계는 개방시스템 검색에서 확인되지 않았다(기관수현황의 분기별 비교로 간접 산출 가능).

## 2. 국민건강보험공단(NHIS): 건강보험통계, 건강보험 빅데이터 플랫폼(맞춤형DB, 표본코호트DB)

### Takeaway
NHIS는 (1) 자율공시·통계연보·지역별 의료이용통계 등 공개 통계, (2) 공공데이터포털의 치과 행위코드별 진료현황 파일, (3) 유료 연구용 DB(표본연구DB·맞춤형연구DB, 치과 명세서 포함)를 제공한다. 가장 세밀한 치과 청구 분석은 (3)을 신청해야 가능하다.

### Cited Findings
- 건강보험 빅데이터 플랫폼(국민건강보험자료 공유서비스, NHISS): [nhiss.nhis.or.kr](https://nhiss.nhis.or.kr/). 제공안내: [bdaba001cv](https://nhiss.nhis.or.kr/bd/ab/bdaba001cv.do), 표본연구DB 신청: [bdaba005iv](https://nhiss.nhis.or.kr/bd/ab/bdaba005iv.do), DB 세부내역: [bdaba002cv](https://nhiss.nhis.or.kr/bd/ab/bdaba002cv.do).
- 표본코호트 DB 진료 테이블에 치과(D) 명세서가 포함된다(의과·보건기관, 치과, 한방, 약국 명세서 구성). — [DB세부내역](https://nhiss.nhis.or.kr/bd/ab/bdaba002cv.do) (검색 결과 요약 기준)
- 연구용 DB 3종: 표본코호트DB, 희귀질병전수DB, 건강검진전수DB. — [데일리팜](https://www.dailypharm.com/user/news/151175)
- 비용(검색 결과 요약, 페이지 간 시점이 다를 수 있음): 표본연구DB는 6일 이하 일 25,000원, 1주~1개월 미만 주 112,500원, 1개월 이상 월 350,000원. 맞춤형연구DB는 제공 수수료 30,000원/GB에 이용기간 수수료 6개월까지 1,200,000원이고 6개월 초과 시 월 200,000원이다. 감면율은 학술연구 50%, 학위논문·정책연구 80%, 공단 연구과제 100%. — [NHISS 제공안내/비용 페이지군](https://nhiss.nhis.or.kr/bd/ab/bdaba001cv.do) (정확한 최신 금액은 신청 화면의 비용계산기로 재확인 필요)
- 심의 승인 후 제공까지 SAS/R 신청은 약 2개월, SPSS/STATA 신청은 약 3개월로 안내한다. — [NHISS 안내](https://nhiss.nhis.or.kr/bd/ab/bdaba001cv.do) (검색 결과 요약 기준)
- 2026년 8월 보도: 공단이 산업계 활용 확대를 위해 국민건강정보 DB에서 100만 명을 무작위 추출·가명처리한 저위험 표본데이터 설명회를 열었다. 신청 절차와 시범사업은 플랫폼 고객지원 공지에 게시된다고 한다. — [메디파나/medifonews 2026.08.05](https://medifonews.com/news/article.html?no=214824) (기사 제목·세부 조건은 미확인)
- 공공데이터포털 파일: '국민건강보험공단_치과 요양기관 행위코드별 진료현황_20231231'. 대상은 치과병원·치과의원, 진료년도 2014~2023, 진료인원(중복제외)과 청구건수, 수가금액은 2024년 6월 심사분까지 반영, CSV+txt 설명을 zip으로 제공, 등록·수정일 2025-06-05. 갱신주기는 미확인(동일 기관 유사 파일은 '수시(1회성)'로 표기되는 경우가 있음). — [data.go.kr/15143761](https://www.data.go.kr/data/15143761/fileData.do)
- NHIS 파일 예: '특정 수가코드(D3021 등) 연도별 시도별 진료현황_20241231'(수가코드 기반이며 D로 시작하는 치과 코드 여부는 미확인) — [data.go.kr/15151301](https://www.data.go.kr/data/15151301/fileData.do); '김해시 매복치아 발치건수 및 요양기관수 현황_20241231' — [data.go.kr/15152346](https://www.data.go.kr/data/15152346/fileData.do)
- 자율공시(건강보험 경영실적): 연도별 요양기관 현황. 검색 요약에 따르면 치과병원은 2021년 234곳에서 2026년 2분기 246곳, 치과의원은 18,589곳에서 19,330곳이다. — [NHIS 연도별 요양기관 현황](https://www.nhis.or.kr/announce/wbhaec11404m01.do)
- 연도별 진료실적 및 요양급여비 추이 공시: [진료실적](https://www.nhis.or.kr/announce/wbhaec11406m01.do), [요양급여비 추이](https://www.nhis.or.kr/announce/wbhaec11403m01.do)
- 2023 지역별 의료이용 통계연보(EXCEL): [NHIS 게시물](https://www.nhis.or.kr/nhis/together/wbhaec06900m01.do?mode=view&articleNo=10848158&article.offset=0&articleLimit=10)
- 건강보험통계연보 지방자치단체통계(건강보험대상자진료실적): [nhiss bdada027cv](https://nhiss.nhis.or.kr/bd/ad/bdada027cv.do)
- KOSIS에 올라온 NHIS 통계표: 시도별 의료인력 현황(TX_35003_A003, 지역별의료이용통계, 인구 천 명당 치과의사 수 등), 시군구별 성별 구강검진 대상 및 수검인원(DT_35007_N035), 일반건강검진 구강검진 종합판정(DT_35007_N149), 65세 이상 다빈도 상병 진료현황(DT_35001_A090111). — [KOSIS 통계표 바로가기 예: DT_35007_N035](https://kosis.kr/statHtml/statHtml.do?orgId=350&tblId=DT_35007_N035&vw_cd=MT_ZTITLE&list_id=&seqNo=&lang_mode=ko&language=kor&obj_var_id=&itm_id=&conn_path=MT_ZTITLE)
- KOSIS 접근 경로(NHIS 기관 트리): [stat.kosis.kr 350_35001](http://stat.kosis.kr/nsieu/view/tree.do?task=branchView&id=350_35001_B*MT_OTITLE&hOrg=350)

### Inferences
- 치과 임플란트·틀니 등 급여 항목의 행위별 수요 분석은 무료 공개 파일(행위코드별 진료현황)로 시작하고, 환자 단위 추적(재내원, 합병증 등)은 표본연구DB로 가는 순서가 현실적이다.
- 건강검진 구강검진 통계(DT_35007_N035, N149)는 예방·검진 수요와 지역 수검률 분석에 쓸 수 있다.

### Gaps
- 맞춤형DB가 치과 데이터를 직접 제공하는 구체적 조건과 최신 비용, 심의 기준은 직접 열람하지 못해 미확인(비용 수치는 검색 요약 기준).
- 2026년 신규 저위험 표본데이터의 치과 명세서 포함 여부는 미확인.
- 위 행위코드별 파일의 갱신주기는 미확인.

## 3. KOSIS(국가통계포털), 국가데이터처 통계에서의 치과 관련 통계표

### Takeaway
통계청은 2025년 10월 1일 국가데이터처로 승격·출범했고 KOSIS는 국가데이터처가 운영한다. KOSIS에서는 '치과' 키워드와 관련 통계표 ID를 확인했다. 특히 서비스업조사 DT_2KB9003은 치과의원 매출 규모를 다루지만 수록기간이 2020~2023년이다.

### Cited Findings
- 통계청은 2025년 10월 1일 '국가데이터처'로 승격 출범했고 기획재정부 소속에서 국무총리 소속으로 변경됐다. 2025-12-30에 산하기관도 '통계'에서 '데이터'로 명칭이 바뀌었다(지방통계청은 지방데이터청). — [뉴시스 2025-09-30](https://mobile.newsis.com/view/NISX20250930_0003350240); [헤럴드경제 2025-12-28](https://www.heraldk.com/article/2025122820170061750)
- KOSIS는 국가데이터처가 제공하는 원스톱 통계 서비스로, 국내·국제·북한 통계를 제공한다. 영문 메타데이터는 300개 이상 기관의 승인통계 1,000종 이상을 담고 있다고 소개한다. 2026-07-08에는 AI 기반 이용자 맞춤형 통계표 생성 시범서비스 안내가 공지됐다. — [KOSIS 소개](https://kosis.kr/serviceInfo/kosisIntroduce.do); [KOSIS 공지](https://kosis.kr/serviceInfo/noticeList.do;jsessionid=OXB6QdVmrOFtCW0f5l2xz_e2Uszc8qkPDrYrrTTL.esvwas1_S11)
- KOSIS 통계표(kosis_local_search 및 table_info로 조회한 통계표 ID와 수록주기):
  - 서비스업조사 '시도/산업/매출액규모별 현황' (국가데이터처, orgId 101, DT_2KB9003): 치과의원 매출액 키워드 매핑, 연간, 수록 2020~2023. — [KOSIS](https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_2KB9003&vw_cd=MT_ZTITLE&list_id=&seqNo=&lang_mode=ko&language=kor&obj_var_id=&itm_id=&conn_path=MT_ZTITLE) (치과의원 산업 분류가 이 표 분류에 실제 포함되는지는 분류항목 미조회로 확인하지 못함)
  - 건강보험통계 '시도별 종별 요양기관 현황' (HIRA, orgId 354, DT_MIRE01): 월 2003.01~2008.12, 분기 2009 1/4~2026 2/4. — [KOSIS](https://kosis.kr/statHtml/statHtml.do?orgId=354&tblId=DT_MIRE01&vw_cd=MT_ZTITLE&list_id=&seqNo=&lang_mode=ko&language=kor&obj_var_id=&itm_id=&conn_path=MT_ZTITLE)
  - 건강보험통계 '치과 연령별 성별 진료비 심사실적' (HIRA, 354, DT_LEE_46). — [KOSIS](https://kosis.kr/statHtml/statHtml.do?orgId=354&tblId=DT_LEE_46&vw_cd=MT_ZTITLE&list_id=&seqNo=&lang_mode=ko&language=kor&obj_var_id=&itm_id=&conn_path=MT_ZTITLE)
  - 보건의료인력실태조사 '전문과목별, 의료기관 유형별 의료기관 근무 치과전문의 수' (보건복지부, 117, DT_117110_B010). — [KOSIS](https://kosis.kr/statHtml/statHtml.do?orgId=117&tblId=DT_117110_B010&vw_cd=MT_ZTITLE&list_id=&seqNo=&lang_mode=ko&language=kor&obj_var_id=&itm_id=&conn_path=MT_ZTITLE)
  - 보건의료인력실태조사 '성별, 시도별, 직역별 의료기관 근무치과의사(일반의/전문의) 연평균 임금' (117, DT_117110_B014). — [KOSIS](https://kosis.kr/statHtml/statHtml.do?orgId=117&tblId=DT_117110_B014&vw_cd=MT_ZTITLE&list_id=&seqNo=&lang_mode=ko&language=kor&obj_var_id=&itm_id=&conn_path=MT_ZTITLE)
  - 지역별의료이용통계 '시도별 의료인력 현황' (NHIS, 350, TX_35003_A003). — [KOSIS](https://kosis.kr/statHtml/statHtml.do?orgId=350&tblId=TX_35003_A003&vw_cd=MT_ZTITLE&list_id=&seqNo=&lang_mode=ko&language=kor&obj_var_id=&itm_id=&conn_path=MT_ZTITLE)
  - 의료서비스이용현황 '의료기관종별 환자 수' (보건복지부, 117, DT_117030_001; 치과방문 비율 키워드). — [KOSIS](https://kosis.kr/statHtml/statHtml.do?orgId=117&tblId=DT_117030_001&vw_cd=MT_ZTITLE&list_id=&seqNo=&lang_mode=ko&language=kor&obj_var_id=&itm_id=&conn_path=MT_ZTITLE)
  - 장애인삶패널조사 '지난 6개월 동안 의료기관 이용 경험' (한국장애인개발원, 438, DT_438001_AD018). — [KOSIS](https://kosis.kr/statHtml/statHtml.do?orgId=438&tblId=DT_438001_AD018&vw_cd=MT_ZTITLE&list_id=&seqNo=&lang_mode=ko&language=kor&obj_var_id=&itm_id=&conn_path=MT_ZTITLE)
  - 구강 관련: 아동및장애인구강건강실태조사(질병관리청, orgId 177) DT_117051_A013(만 12세 우식영구치지수 등), DT_117051_A005(만 5세 우식유치지수 등); 장애인건강보건통계(117) DT_117102_A016(장애인 구강검진 종합소견). — [KOSIS DT_117051_A013](https://kosis.kr/statHtml/statHtml.do?orgId=177&tblId=DT_117051_A013&vw_cd=MT_ZTITLE&list_id=&seqNo=&lang_mode=ko&language=kor&obj_var_id=&itm_id=&conn_path=MT_ZTITLE)
- 데이터 형태: 통계표 조회·다운로드(웹), KOSIS OpenAPI(별도 신청). — [KOSIS 소개](https://kosis.kr/serviceInfo/kosisIntroduce.do) (OpenAPI 신청 절차의 세부 내용은 미확인)

### Inferences
- 치과의원 수(DT_MIRE01, 분기), 치과 인력(TX_35003_A003, DT_117110_B010·B014), 치과 매출 규모(DT_2KB9003) 3종을 결합하면 지역별 공급, 인력, 매출 구조를 한 번에 볼 수 있다. 다만 서로 다른 통계표를 연결할 때는 정의와 모집단이 다를 수 있다는 KOSIS 연결 주의사항을 따라야 한다.
- 위 통계표 ID는 KOSIS MCP 로컬 카탈로그의 키워드 매핑 결과다. '치과' 키워드의 전체 통계표 목록을 보증하지는 않는다.

### Gaps
- KOSIS 전체검색(kosis_search)은 60초 타임아웃으로 실패해 '치과' 전체 검색 결과 목록은 확보하지 못했다.
- 광업제조업조사, 사회조사, 가계동향조사 등에서 치과 관련 세부 통계표는 확인하지 못했다. 서비스업조사 이외의 국가데이터처 통계는 미확인.
- DT_2KB9003의 분류(치과의원 산업코드 포함 여부, 최신 연도 갱신)는 미확인.

## 4. 질병관리청(국민건강영양조사, 아동·장애인구강건강실태조사, 국가건강정보포털), 보건복지부 통계

### Takeaway
구강건강 상태(우식, 치주질환, 구강건강행태)는 질병관리청의 국민건강영양조사(원시자료 공개)와 아동·장애인구강건강실태조사가 핵심이며, 인력 현황은 보건복지부의 공공데이터 파일·보건복지통계연보·보건의료인력실태조사로 확인한다.

### Cited Findings
- 국민건강영양조사 누리집: [knhanes.kdca.go.kr](https://knhanes.kdca.go.kr/knhanes/main.do). 조사수행, 조사표, 원시자료, 통계집, 국민건강통계플러스, 추적조사를 제공하고 원시자료 이용지침서/코드자료, 학술연구자료 신청 안내 메뉴가 있다. 질병관리청 소개 페이지: [kdca.go.kr/kdca/3367](https://www.kdca.go.kr/kdca/3367/subview.do)
- 2024년 국민건강영양조사 통계집과 원시자료는 2025-12-31부터 공개됐고 원시자료는 약 800개 변수를 포함한다. 치아상태, 치료필요, 보철물 상태 등 구강 항목이 목록에 있다고 한다(어느 조사 기준 목록인지는 불명확). — [질병관리청 보도참고자료 2025-12-31](https://www.kdca.go.kr/bbs/kdca/42/304276/download.do)
- 2025년 국민건강영양조사 주요 결과는 2026-09-30 발표됐고, 상세 통계보고서·원시자료는 2026년 12월 공개 예정이다. — [질병관리청 보도자료 2026-09-30](https://www.kdca.go.kr/bbs/kdca/42/310041/download.do) (예정이므로 미래 시점 계획이며 변경 가능)
- 구강 항목은 2007년부터 1세 이상을 대상으로 한 국민건강영양조사에 포함되어 있다. — [검색 결과 요약 근거: Journal of Korean Academy of Oral Health 논문 목록](https://synapse.koreamed.org/articles/1110943)
- 대국민 건강통계 시각화(예: 칫솔질 지표): [chs.kdca.go.kr 칫솔질 지표](https://chs.kdca.go.kr/cdhs/biz/pblcVis/details.do?ctgrSn=58) (지역사회건강조사 기반 시각화 페이지로 보이나 데이터 출처 정확한 표기는 미확인)
- 아동구강건강실태조사(2024년, 2025-07 발표): 5세 유치와 12세 영구치 약 2만 명 조사. 유치 우식 경험률 58.3%, 영구치 우식 경험률 60.3%, 점심 후 칫솔질 실천율 22.6%, 치과 진료 수진율 72.1%, 미충족 치과치료 필요율 14.7%. — [Daum/연합 보도 2025-07-01](https://v.daum.net/v/20250701120013150); [질병관리청 자료](https://kdca.go.kr/bbs/kdca/42/308085/download.do)
- 장애인구강건강실태조사(2025년, 2026-06 발표): 등록 장애인 1,988명 대상, 구강보건법 제9조 근거. 통계집·원시자료는 별도 누리집에서 공개된다고 보도(누리집 URL 미확인). — [세계일보 2026-07-01](https://www.segye.com/newsView/20260701515815)
- KOSIS에서도 아동및장애인구강건강실태조사 통계표를 볼 수 있다(DT_117051_A013, DT_117051_A005; 3번 참조).
- 국가건강정보포털(질병관리청): 구강병 예방, 충치, 치주질환 등 건강정보 콘텐츠. — [health.kdca.go.kr 구강병](https://health.kdca.go.kr/healthinfo/biz/health/gnrlzHealthInfo/gnrlzHealthInfo/gnrlzHealthInfoView.do?cntnts_sn=6291) (통계 데이터셋이 아니라 정보 콘텐츠로 보이며 통계 제공 범위는 미확인)
- 보건복지부 구강보건사업 정책: 제2차 구강보건사업 기본계획(2022~2026) 발표(구강보건의 날 보도자료). — [mohw.go.kr 보도자료](https://mohw.go.kr/board.es?act=view&bid=0027&list_no=371733&mid=a10503000000)
- 보건복지통계연보: 2024년판(2024-12-27 게시), 2023년판(2023-12-20 게시) 등 연 1회, PDF/HWPX 제공. 치과 의료기관·인력 표의 정확한 위치는 미확인. — [2024 보건복지통계연보](https://www.mohw.go.kr/board.es?mid=a10411010100&bid=0019&tag=&act=view&list_no=1484109)
- 보건의료인력 실태조사 결과: 20개 직종(치과위생사 포함) 근로현황·보수 조사. — [mohw.go.kr 보도자료](https://mohw.go.kr/board.es?act=view&bid=0027&list_no=372084&mid=a10503000000)
- 공공데이터포털: 보건복지부 보건의료인 면허(자격) 신규등록현황(2003~2025, 치과의사·치과위생사 포함) — [data.go.kr/15093758](https://www.data.go.kr/data/15093758/fileData.do); 면허 말소현황 20241231(사망 확인 기준) — [data.go.kr/15093759](https://www.data.go.kr/data/15093759/fileData.do?recommendDataYn=Y)
- 공공데이터포털: 보건복지부 병원 및 의원 수(의료기관 종류별·시도별) 20241231, 치과의원이 별도 항목으로 포함 — [data.go.kr/15127855](https://www.data.go.kr/data/15127855/fileData.do?recommendDataYn=Y); 병원 종사 의료인력 수(시도별) 20231231, 치과의사 항목 포함. 2024년부터 '의료기관 종사 의료인력 수_시도별'로 개편됐다고 안내 — [data.go.kr/15127873](https://www.data.go.kr/data/15127873/fileData.do?recommendDataYn=Y)
- 치과의사전문의 현황(2025년 4월 기준) 사전정보공표 — [mohw.go.kr](https://mohw.go.kr/board.es?act=view&bid=0046&cg_code=&list_depth=1&list_no=1485227&mid=a10107010100&tag=)
- 연도별 치과의사 면허인 통계는 2007년 게시본이라 최신 수치는 아니다. — [mohw.go.kr](https://mohw.go.kr/board.es?act=view&bid=0020&list_no=264291&mid=a10412000000&nPage=34&tag=)

### Inferences
- 구강건강 '수요 측' 지표(우식 경험률, 치주질환 유병률, 미충족 치과치료율)는 질병관리청 조사에서, '공급 측' 지표(면허 인력, 기관 수)는 보건복지부·HIRA에서 얻어 결합하는 구조가 된다.
- 치과위생사 면허 신고 인원(현재 활동 인원)은 면허 신규·말소 파일만으로는 산출이 어렵고, 건강보험 청구 기준 활동 인력은 HIRA 의료인력통계(15066021)가 더 직접적이다.

### Gaps
- 국민건강영양조사 치주질환 지표의 최신 연도 수치와 구강검진 변수명은 원시자료 이용지침서를 확인하지 못해 미확인.
- 장애인구강건강실태조사 별도 누리집 URL 미확인. 아동구강건강실태조사의 전용 데이터 포털 여부도 미확인(KOSIS와 질병관리청 보도·발간자료로 확인).
- 보건복지부 통계포털(stat.mohw.go.kr 등)은 검색 결과에서 확인되지 않아 미확인.

## 5. 의료기기 데이터: 식약처 통계, 의료기기정보포털(UDI), 한국의료기기안전정보원, 관세청·K-stat

### Takeaway
치과 의료기기는 식약처의 허가/품목 정보(공공데이터포털 API)와 생산·수출입 실적 통계, 관세청 HS 기반 무역통계(HS 9018 계열 치과용 기기)로 입체적으로 볼 수 있다. 다만 치과 품목만 따로 정리한 공식 연보는 확인하지 못했다.

### Cited Findings
- 식약처 의료기기 생산·수출·수입 실적: 식약처 대표 누리집의 통계 메뉴(통계간행물 > 통계자료)에 게재된다. 게시판: [mfds.go.kr/brd/m_386](https://www.mfds.go.kr/brd/m_386/list.do). 2024년 의료기기 생산액 11조 4,267억 원, 수출 7조 1,700억 원, 수입 6조 2,877억 원(디지털의료기기 별도 집계). — [메디파나/메디고뉴스 등 보도: medifonews 2026.06.12](https://medifonews.com/news/article.html?no=213914) (치과 분야 분리 수치는 해당 보도에 없음)
- 연간 실적 보고 안내(2025년 의료기기 생산·수출·수입 등 실적 보고, 체외진단·디지털의료기기 포함): [mfds.go.kr 공지](https://mfds.go.kr/brd/m_841/view.do?seq=45780). 업체가 매년 초 보고하는 구조다(보고 접수 주체는 한국의료기기산업협회로 안내되나 정확한 문구는 미확인).
- 의료기기정보포털(UDI 포털): 무역통계 게시물에 'HS Code별 의료기기 수출입 동향'(의료용품, 국가별) 시리즈가 있다(2017~2019년 사례 확인). — [udiportal 무역통계 게시물](https://udiportal.mfds.go.kr/brd/view/P05_05_01?ntceSn=78). 검색 기능: [udiportal 의료기기 정보검색](https://udiportal.mfds.go.kr/search/brd/P99_03?keyword=%EC%B9%98%EA%B3%BC%EC%9A%A9%EC%9D%98%EB%A3%8C%EA%B8%B0%EA%B8%B0&searchYn=Y) (키워드 '치과용의료기기' 검색 예).
- 업체/제품정보 검색 메뉴는 2024-01-12까지만 유지하고 '의료기기 안심책방'으로 일원화한다고 안내됐다. — [emedi.mfds.go.kr UDI 포털](https://emedi.mfds.go.kr/msismext/udi/min/mainView.do)
- 공공데이터포털 식약처 OpenAPI: 의료기기 품목허가 정보 — [15057456](https://www.data.go.kr/data/15057456/openapi.do); 의료기기 품목정보 — [15073906](https://www.data.go.kr/data/15073906/openapi.do); 통합업체 정보(사업장 주소, 인허가일, 폐업일 등) — [15117407](https://www.data.go.kr/data/15117407/openapi.do); UDI/EDI 정보 조회 서비스 — [15138675](https://www.data.go.kr/data/15138675/openapi.do?recommendDataYn=Y). 치과용 품목 필터링으로 집계 가능(치과 분류 코드 자체는 미확인).
- 한국보건산업진흥원(KHIDI)의 의료기기산업 통계표(시장규모, 생산, 수출입, 고용 등) 공공데이터포털 파일: 2021-02-28 버전 [data.go.kr/3081173](https://www.data.go.kr/data/3081173/fileData.do), 2021-10-07 버전 [data.go.kr/15091681](https://www.data.go.kr/data/15091681/fileData.do?recommendDataYn=Y). 등록 시점이 2021년이라 오래됨.
- 관세청: 공공데이터포털 '관세청_품목별 수출입실적(GW)' OpenAPI(HS 2·4·6·10단위, 월 1회 갱신) — [15101609](https://www.data.go.kr/data/15101609/openapi.do); '품목별 국가별 수출입실적(GW)'(조회기간 1년 이내, 품목·국가 코드 지정) — [15100475](https://www.data.go.kr/data/15100475/openapi.do); HS부호 단위별 품목명 파일 — [15130660](https://www.data.go.kr/data/15130660/fileData.do?recommendDataYn=Y)
- 관세청 빅데이터 포털(수출입트렌드, HS 10단위 조회): [bigdata.customs.go.kr](https://bigdata.customs.go.kr/web/cten/2/ctenView.do?tab=1). 무역통계 홈페이지 활용법: [customs.go.kr](https://www.customs.go.kr/kcs/na/ntt/selectNttInfo.do?mi=10600&bbsId=2280&nttSn=10141578&nttSnUrl=66d660b3d86d06959c8f4ad9b5c4f389)
- K-stat 무역통계(한국무역협회): [stat.kita.net](https://stat.kita.net/). 시군구 기준 HSK 10단위 품목 통계는 비공개라는 제한이 있다는 안내가 있다(검색 결과 요약 기준). 무역통계 보조 사이트: [bandtrass.or.kr](https://www.bandtrass.or.kr/customs/total.do?command=CUS001View&viewCode=CUS00201)
- HS 9018 구조: 한국 세번표에서 9018 하위에 치과용 드릴 엔진(9018.41), 기타 치과용 기기(9018.49) 등이 있다(참고 자료로 확인한 외부 정리 사이트이며 공식 세번표가 아님). — [treayo.com Korea HS 9018](https://treayo.com/en/hs/korea/h/9018) (한국 관세청 공식 세번표에서의 10단위 분류는 미확인)
- KHIDI 의료기기산업 통계: 의료기기산업 정보 페이지 [khidi.or.kr](https://www.khidi.or.kr/board?menuId=MENU01518&siteId=SITE00004), 보건산업통계 포털 KHISS [khiss.go.kr](https://khiss.go.kr/) (의료기기 통계지표 [khiss.go.kr](https://www.khiss.go.kr/board?menuId=MENU00318&siteId=null)), 2024 보건산업 통계집 [khidi.or.kr](https://www.khidi.or.kr/board/view?linkId=48923524&menuId=MENU00086)
- 한국의료기기안전정보원: 이번 조사의 검색 결과에서는 별도 치과 통계 페이지를 확인하지 못했다.

### Inferences
- '치과용' 규모를 보려면 (a) 식약처 품목허가 API에서 치과용 품목을 필터링해 업체·품목 수를 집계하고, (b) 관세청 API로 HS 9018.41/9018.49 및 치과 재료(HS 3006.40 등 코드는 미확인) 수출입을 조회하는 조합이 현실적이다.
- 식약처 연보의 대분류는 치과재료가 별도 분류로 보도된 사례가 있어(2018년으로 추정) 최신 연보 PDF에서 치과 분류를 확인할 가치가 있다.

### Gaps
- 식약처 연보 PDF 본문에서 치과 품목(치과재료·치과용 기구) 최신 연도 생산/수출입액은 확인하지 못했다. 보도 요약에서 본 치과재료 수치(생산 약 1억 9천만 개, 수출 약 383십억 원, 수입 약 133십억 원)는 연도가 불분명(2018년으로 추정)해 인용하지 않는다.
- 한국의료기기안전정보원 통계 메뉴, 의료기기산업 종합정보시스템(KHIDI)의 치과 세부 통계는 미확인.
- 관세청 unipass 무역통계 조회 화면 구조 및 K-stat 치과 HS 코드 조회 방법은 직접 열람하지 못해 미확인.

## 6. 공공데이터포털(data.go.kr) 치과 관련 API/파일데이터

### Takeaway
공공데이터포털에는 HIRA, NHIS, 보건복지부, 식약처, 관세청, 국세청, 행정안전부의 치과 관련 파일·API가 흩어져 있다. 회원가입 후 무료로 활용하며 API는 활용신청과 키 발급이 필요하다.

### Cited Findings
- 보건복지부 병원 및 의원 수(종류별·시도별) 20241231 — [15127855](https://www.data.go.kr/data/15127855/fileData.do?recommendDataYn=Y)
- 보건복지부 병원 종사 의료인력 수(시도별) 20231231 — [15127873](https://www.data.go.kr/data/15127873/fileData.do?recommendDataYn=Y)
- 보건복지부 보건의료인 면허 신규등록현황 20251231 — [15093758](https://www.data.go.kr/data/15093758/fileData.do)
- HIRA 의료인력통계 20250331 — [15066021](https://www.data.go.kr/data/15066021/fileData.do); 전국 병의원 및 약국 현황 20251231 — [15051059](https://www.data.go.kr/data/15051059/fileData.do); 병원정보서비스 OpenAPI — [15094093](https://www.data.go.kr/data/15094093/openapi.do)
- NHIS 치과 요양기관 행위코드별 진료현황 20231231 — [15143761](https://www.data.go.kr/data/15143761/fileData.do)
- 식약처 의료기기 품목허가·품목정보·통합업체 API — [15057456](https://www.data.go.kr/data/15057456/openapi.do), [15073906](https://www.data.go.kr/data/15073906/openapi.do), [15117407](https://www.data.go.kr/data/15117407/openapi.do)
- 관세청 품목별 수출입실적 API — [15101609](https://www.data.go.kr/data/15101609/openapi.do)
- 국세청 사업자현황(연령별·성별·존속연수별, 20260731 기준) — [15061120](https://www.data.go.kr/data/15061120/fileData.do), [15061119](https://www.data.go.kr/data/15061119/fileData.do), [15061121](https://www.data.go.kr/data/15061121/fileData.do); 100대 생활업종 신규사업자 현황(업종별 월별) 20251231 — [15048949](https://www.data.go.kr/data/15048949/fileData.do) (신규사업자 자료에 병·의원 13개 업종이 서비스업으로 포함된다는 검색 요약. 치과의원 포함 여부는 미확인)
- 행정안전부 지방행정 인허가: 지방정부의 업종별 인허가 정보를 공공데이터포털에서 통합 개방(보도자료). 전국 병원 데이터셋은 보건복지부 의료기관정책과 소관이며 치과의원·치과병원 모두 포함된다는 설명이 데이터셋 메타에 있다. 좌표계가 데이터셋마다 다르고(EPSG:5174, EPSG:2097 등) 위경도가 없는 경우도 있다. — [행안부 보도자료](https://www.mois.go.kr/frt/bbs/type010/commonSelectBoardArticle.do?bbsId=BBSMSTR_000000000008&nttId=123399); [data.go.kr 메타 15156257](https://www.data.go.kr/biz/dcat/metadata/15156257.do); [data.go.kr 메타 15115763](https://www.data.go.kr/biz/dcat/metadata/15115763.do)
- 이 외 지자체별 병원/의원 현황 파일이 다수 존재한다(예: 전남광주통합특별시 병원 의원현황 20250723). — [15069181](https://www.data.go.kr/data/15069181/fileData.do?recommendDataYn=Y)
- API 이용 조건(HIRA 사례): 회원가입·활용신청 필요, REST/XML, 무료, 개발계정 자동승인, 운영계정 심의. — [15094093](https://www.data.go.kr/data/15094093/openapi.do)

### Inferences
- 개별 치과 위치·개폐업 시계열은 인허가 데이터(localdata/공공데이터포털)로, 건강보험 기준 활동 기관은 HIRA 현황으로 구성해 서로 교차검증하면 폐업 누락이나 지연 문제를 줄일 수 있다.

### Gaps
- 공공데이터포털 내 '치과' 키워드 전체 데이터셋 목록(포털 검색 화면)은 직접 조회하지 못했다. 위 목록은 검색 결과로 노출된 항목만이다.
- 행정안전부 전국 '치과의원' 별도 인허가 데이터셋 번호는 미확인(전국 병원 데이터셋 설명에 치과 포함이라는 문구만 확인).

## 7. 한국보건산업진흥원(KHIDI), 한국보건사회연구원(KIHASA), 한국보건의료연구원(NECA) 등 연구기관

### Takeaway
KHIDI의 보건산업통계(KHISS)와 보건산업 통계집이 의료기기 산업 쪽 통계 원천이다. KIHASA와 NECA는 이번 검색 범위에서 치과 전용 통계 사이트를 확인하지 못했다.

### Cited Findings
- KHISS 보건산업통계 포털: 총괄, 의약품, 의료기기, 화장품, 의료서비스 분야별 통계지표와 KSIC-10 기반 보건산업분류체계, 통계용어사전을 제공한다. — [khiss.go.kr](https://khiss.go.kr/)
- KHIDI는 매년 '보건산업 통계집'을 발간하며 의료기기산업이 포함된다. 최신 확인본은 2024년판. — [2024 보건산업 통계집](https://www.khidi.or.kr/board/view?linkId=48923524&menuId=MENU00086); [2023 보건산업 통계집(KHISS)](https://khiss.go.kr/board/view?pageNum=1&rowCnt=10&no1=344&linkId=176245&menuId=MENU00309&schType=0)
- 통계 항목: 시장규모(국내·국외), 생산, 수출입, 고용, 보건산업 연구개발 실태조사(의료기기). 생산·수출입은 주로 식약처 실적 보고 기반이고 시장규모는 KHIDI 분석 보고서 기반이다. — [KHISS 의료기기 통계지표](https://www.khiss.go.kr/board?menuId=MENU00318&siteId=null)
- HIRA 연구보고서 저장소에 치과 분야 적정성 평가 방안 연구(2016) 등 치과 관련 보고서가 있다. — [repository.hira.or.kr 치과분야 적정성 평가 방안 및 기준 개발연구](https://repository.hira.or.kr/bitstream/2019.oak/1710/2/%EC%B9%98%EA%B3%BC%EB%B6%84%EC%95%BC%20%EC%A0%81%EC%A0%95%EC%84%B1%20%ED%8F%89%EA%B0%80%20%EB%B0%A9%EC%95%88%20%EB%B0%8F%20%EA%B8%B0%EC%A4%80%20%EA%B0%9C%EB%B0%9C%EC%97%B0%EA%B5%AC.pdf)

### Inferences
- 치과산업 시장규모 추정에는 KHIDI 의료기기 시장규모 보고서(일반 의료기기 단위)를 기본으로 하고, 치과 분류는 식약처 연보와 관세청 HS 코드로 별도 보완해야 할 가능성이 크다.

### Gaps
- KIHASA(한국보건사회연구원)와 NECA(한국보건의료연구원)의 치과·구강보건 보고서 제공 사이트는 이번 검색에서 확인되지 않았다(미확인).
- KHISS 치과 전용 지표 존재 여부 미확인(의료기기 일반 지표만 확인).

## 8. 부가 데이터원: 지방행정인허가데이터개방(localdata), 국세청 국세통계, 한국은행 ECOS

### Takeaway
localdata는 치과의원 단위 인허가·개폐업 정보를 제공하며 2026년 1월 이후 공공데이터포털로 통합 개방하는 방향이다. 국세통계(TASIS)와 국세청 사업자현황은 치과의원 소득·사업자 구조를 보여주고, ECOS는 치과 전용 지표를 확인하지 못했다.

### Cited Findings
- 지방행정인허가데이터개방(LOCALDATA): API이용가이드 [localdata.go.kr/devcenter/apiGuide.do](https://www.localdata.go.kr/devcenter/apiGuide.do?menuNo=20002), API신청 [applyGroupApi](https://www.localdata.go.kr/devcenter/applyGroupApi.do?menuNo=20002). OPEN API는 변동분만 호출 가능, 전체 자료는 다운로드 페이지를 이용하며 자치단체 등록 데이터를 이틀 전 기준으로 매일 갱신한다고 안내(해당 문구는 과거 페이지일 수 있어 현재 유효성은 확인 필요).
- 행정안전부는 지방정부 업종별 인허가·생활편의 정보를 공공데이터포털(data.go.kr)에서 통합 공개한다고 밝혔다(2026-01 보도). 이관 시점과 localdata 존속 여부는 확인되지 않았다. — [행안부 보도자료](https://www.mois.go.kr/frt/bbs/type010/commonSelectBoardArticle.do?bbsId=BBSMSTR_000000000008&nttId=123399); [경향신문 2026-01-25](https://www.khan.co.kr/article/202601251400011/)
- 국세통계포털(TASIS): '통계로 보는 소득' 메뉴 등 — [tasis.nts.go.kr 테마통계](https://tasis.nts.go.kr/websquare/websquare.html?w2xPath=%2Fcm%2Findex.xml&menuCode=48&menuScrnId=UTWEPFCA01). 의료업 업종별 수입금액 표의 세부 구성은 직접 확인하지 못했다.
- 치과의원 소득·매출 관련 보도(국세청 2023년 귀속 종합소득세 자료 기반): 치과의원 상위 5%의 연매출 20억 4천만 원 이상, 전국 치과의원 평균 연매출 7억 7,860만 원(전년 대비 5.12% 증가), 충북이 9억 400만 원으로 최고. — [치의신보(dentalnews) 보도](https://www.dentalnews.or.kr/mobile/article.html?no=45588) (2차 보도 인용이며 국세청 원본 표 URL은 미확인)
- 국세청 사업자현황 데이터는 공공데이터포털에서 제공(6번 참조).
- 한국은행 경제통계시스템 ECOS: [ecos.bok.or.kr](https://ecos.bok.or.kr/). 소비자물가지수(2020=100) 통계코드 901Y009 등 OpenAPI가 있다. — [ECOS API 샘플](http://ecos.bok.or.kr/api/StatisticItemList/sample/xml/kr/1/1/901Y009/) (치과 진료 관련 세부 품목 지수는 이번 검색에서 확인하지 못했다)

### Inferences
- 치과 경영 환경(매출, 업력, 지역 분포)은 국세청 자료 + 인허가 데이터 + HIRA 기관 수의 결합으로 설명할 수 있다. 다만 국세청 매출은 신고 기준 평균이라 보험청구 기준 진료비와 정의가 다르다.
- 치과 진료 가격 동향은 소비자물가조사(국가데이터처, KOSIS) 품목별 지수를 확인하는 편이 ECOS보다 직접적일 가능성이 있다(미확인).

### Gaps
- TASIS에서 '치과의원' 업종 코드 단위 통계표 존재 여부와 접근 경로, 갱신 시점은 미확인(보도 인용 수치만 확인).
- localdata.go.kr의 현재 서비스 상태(통합 이후 유지 여부)는 미확인.
- ECOS 내 치과 관련 전용 시계열 미확인.
