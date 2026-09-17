# DB2ADMIN.PRODUCTIONDEMANDBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `PRODUCTION` (high confidence — table name starts with 'PRODUCTION')
- **Roles**: `staging_mirror`
- **Columns**: 235
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 87197

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PREVIOUSALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 3 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 4 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 5 | `TEMPLATECODE` | CHAR(3) |  |  |  |  |
| 6 | `TYPE` | CHAR(2) |  |  |  |  |
| 7 | `COUNTERCODE` | CHAR(8) |  |  |  |  |
| 8 | `CODE` | CHAR(15) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 9 | `ORDERDATE` | DATE |  |  |  |  |
| 10 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 11 | `COLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 12 | `INTERNALORDERGROUPCODE` | CHAR(15) |  |  |  |  |
| 13 | `DESCRIPTION` | VARCHAR(200) |  |  | description |  |
| 14 | `PLANTCODE` | CHAR(8) |  |  |  |  |
| 15 | `PRODUCTIONRESPONSIBLECODE` | CHAR(50) |  |  |  |  |
| 16 | `REFERENCEDATE` | DATE |  |  |  |  |
| 17 | `SESSIONSTEP` | CHAR(2) |  |  |  |  |
| 18 | `PLANNERCODE` | CHAR(50) |  |  |  |  |
| 19 | `FIRSTISSUEDONE` | CHAR(2) |  |  |  |  |
| 20 | `INITIALIZEREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 21 | `MAINRESOURCECODE` | CHAR(8) |  |  |  |  |
| 22 | `CUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 23 | `CUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 24 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 25 | `EXTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 26 | `INTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 27 | `UPDATEWAREHOUSEAVAILABILITY` | SMALLINT | NOT NULL |  |  |  |
| 28 | `PRDDEMANDSTOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 29 | `ENTRYWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 30 | `ENTRYLOCWHSZONEPHYWHSCODE` | CHAR(8) |  |  |  |  |
| 31 | `ENTRYLOCATIONWAREHOUSEZONECODE` | CHAR(3) |  |  |  |  |
| 32 | `ENTRYLOCATIONCODE` | CHAR(10) |  |  |  |  |
| 33 | `WAREHOUSEWIPCODE` | CHAR(8) |  |  |  |  |
| 34 | `WIPCOSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 35 | `DIRTYFIELD` | CHAR(20) |  |  |  |  |
| 36 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 37 | `ITEMCODE` | VARCHAR(120) |  |  |  |  |
| 38 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 39 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 40 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 41 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 42 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 43 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 44 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 45 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 46 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 47 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 48 | `VIRTUALITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 49 | `VIRTUALITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 50 | `QUALITYCODE` | DECIMAL(2,0) |  |  |  |  |
| 51 | `PREVIOUSQUALITYCODE` | DECIMAL(2,0) |  |  |  |  |
| 52 | `PREVIOUSENTRYWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 53 | `PREVIOUSPROJECTCODE` | CHAR(20) |  |  |  |  |
| 54 | `PREVIOUSSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 55 | `PREVIOUSCUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 56 | `PREVIOUSCUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 57 | `BOMNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 58 | `BOMSUBCODE01` | CHAR(20) |  |  |  |  |
| 59 | `BOMVIRTUALRETURNSUBCODE` | CHAR(30) |  |  |  |  |
| 60 | `BOMSUBCODE02` | CHAR(10) |  |  |  |  |
| 61 | `BOMSUBCODE03` | CHAR(10) |  |  |  |  |
| 62 | `BOMSUBCODE04` | CHAR(10) |  |  |  |  |
| 63 | `BOMSUBCODE05` | CHAR(10) |  |  |  |  |
| 64 | `BOMSUBCODE06` | CHAR(10) |  |  |  |  |
| 65 | `BOMSUBCODE07` | CHAR(10) |  |  |  |  |
| 66 | `BOMSUBCODE08` | CHAR(10) |  |  |  |  |
| 67 | `BOMSUBCODE09` | CHAR(10) |  |  |  |  |
| 68 | `BOMSUBCODE10` | CHAR(10) |  |  |  |  |
| 69 | `BOMSUFFIXCODE` | CHAR(20) |  |  |  |  |
| 70 | `ROUTINGNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 71 | `RTGSUBCODE01` | CHAR(20) |  |  |  |  |
| 72 | `RTGVIRTUALRETURNSUBCODE` | CHAR(30) |  |  |  |  |
| 73 | `RTGSUBCODE02` | CHAR(10) |  |  |  |  |
| 74 | `RTGSUBCODE03` | CHAR(10) |  |  |  |  |
| 75 | `RTGSUBCODE04` | CHAR(10) |  |  |  |  |
| 76 | `RTGSUBCODE05` | CHAR(10) |  |  |  |  |
| 77 | `RTGSUBCODE06` | CHAR(10) |  |  |  |  |
| 78 | `RTGSUBCODE07` | CHAR(10) |  |  |  |  |
| 79 | `RTGSUBCODE08` | CHAR(10) |  |  |  |  |
| 80 | `RTGSUBCODE09` | CHAR(10) |  |  |  |  |
| 81 | `RTGSUBCODE10` | CHAR(10) |  |  |  |  |
| 82 | `RTGSUFFIXCODE` | CHAR(20) |  |  |  |  |
| 83 | `SPLITTINGMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 84 | `PRODUCTIONGROUPCODE` | CHAR(3) |  |  |  |  |
| 85 | `BOXHIDEUOM` | SMALLINT | NOT NULL |  |  |  |
| 86 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 87 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 88 | `BASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 89 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 90 | `USERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 91 | `USERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 92 | `BASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 93 | `BASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 94 | `USERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 95 | `USERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 96 | `PREVIOUSBASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 97 | `PREVIOUSBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 98 | `PREVIOUSBASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 99 | `PREVIOUSBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 100 | `PREVIOUSUSERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 101 | `PREVIOUSUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 102 | `PREVIOUSUSERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 103 | `PREVIOUSUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 104 | `PREVIOUSUSERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 105 | `PREVIOUSUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 106 | `USERPRIMARYUOMVIRTUALCODE` | CHAR(3) |  |  |  |  |
| 107 | `BASEPRIMARYUOMVIRTUALCODE` | CHAR(3) |  |  |  |  |
| 108 | `USERSECONDARYUOMVIRTUALCODE` | CHAR(3) |  |  |  |  |
| 109 | `BASESECONDARYUOMVIRTUALCODE` | CHAR(3) |  |  |  |  |
| 110 | `USERPACKAGINGUOMVIRTUALCODE` | CHAR(3) |  |  |  |  |
| 111 | `FINALUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 112 | `FINALBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 113 | `FINALUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 114 | `FINALBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 115 | `FINALUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 116 | `ENTEREDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 117 | `ENTEREDBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 118 | `ENTEREDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 119 | `ENTEREDBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 120 | `ENTEREDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 121 | `UOMTYPE` | CHAR(2) |  |  |  |  |
| 122 | `STDPRODUCTIONBATCH` | DECIMAL(15,5) |  |  |  |  |
| 123 | `STDPRODUCTIONBATCHUOMCODE` | CHAR(3) |  |  |  |  |
| 124 | `QUANTITYPERPERIOD` | DECIMAL(15,5) |  |  |  |  |
| 125 | `NUMBEROFPERIODS` | INTEGER | NOT NULL |  |  |  |
| 126 | `INITIALPLANNEDDATE` | DATE |  |  |  |  |
| 127 | `FINALPLANNEDDATE` | DATE |  |  |  |  |
| 128 | `INITIALSCHEDULEDDATE` | DATE |  |  |  |  |
| 129 | `FINALSCHEDULEDDATE` | DATE |  |  |  |  |
| 130 | `INITIALEFFECTIVEDATE` | DATE |  |  |  |  |
| 131 | `FINALEFFECTIVEDATE` | DATE |  |  |  |  |
| 132 | `DESTINATIONORDER` | CHAR(2) |  |  |  |  |
| 133 | `DLVSALORDLINESALORDCNTCODE` | CHAR(8) |  |  |  |  |
| 134 | `DLVSALORDERLINESALESORDERCODE` | CHAR(15) |  |  |  |  |
| 135 | `DLVSALESORDERLINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 136 | `DLVSALESORDERLINEORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 137 | `DLVSALORDLINECMPORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 138 | `DELIVERYDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 139 | `RESERVATIONORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 140 | `RESERVATIONORDERCODE` | CHAR(15) |  |  |  |  |
| 141 | `RESERVATIONRESERVATIONLINE` | DECIMAL(7,0) |  |  |  |  |
| 142 | `ORIGDLVSALORDLINESALORDCNTCOD` | CHAR(8) |  |  |  |  |
| 143 | `ORIGDLVSALORDLINESALORDERCODE` | CHAR(15) |  |  |  |  |
| 144 | `ORIGDLVSALORDERLINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 145 | `ORIGDLVSALORDLINEORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 146 | `ORIGDLVSALORDLINECMPORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 147 | `ORIGDELIVERYDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 148 | `INTDLVINTORDLINEINTORDCNTCODE` | CHAR(8) |  |  |  |  |
| 149 | `INTDLVINTORDLINEINTORDERCODE` | CHAR(15) |  |  |  |  |
| 150 | `INTDLVINTORDERLINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 151 | `INTDLVINTORDLINEORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 152 | `INTDELIVERYDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 153 | `INTDOCINTDOCPRVCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 154 | `INTDOCINTDOCPROVISIONALCODE` | CHAR(15) |  |  |  |  |
| 155 | `INTDOCUMENTORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 156 | `INTDOCUMENTORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 157 | `EXTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 158 | `INTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 159 | `CURRENTSTATUS` | CHAR(2) |  |  |  |  |
| 160 | `RUNMANUALCLOSTEPRESERVATION` | SMALLINT | NOT NULL |  |  |  |
| 161 | `RUNMANUALCLOSURE` | SMALLINT | NOT NULL |  |  |  |
| 162 | `RUNMANUALREOPEN` | SMALLINT | NOT NULL |  |  |  |
| 163 | `PREVIOUSPROGRESSSTATUS` | CHAR(2) |  |  |  |  |
| 164 | `PROGRESSSTATUS` | CHAR(2) |  |  |  |  |
| 165 | `FULLITEMIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 166 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 167 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 168 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 169 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 170 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 171 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 172 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 173 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 174 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 175 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 176 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 177 | `MANUALCLOSUREREASON` | INTEGER | NOT NULL |  |  |  |
| 178 | `CLOSUREDATE` | DATE |  |  |  |  |
| 179 | `SECQTYNOTCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 180 | `PACKQTYNOTCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 181 | `RECALCULATEFULLCHAIN` | SMALLINT | NOT NULL |  |  |  |
| 182 | `INITIALPLANNEDSCHEDULEDDATE` | DATE |  |  |  |  |
| 183 | `FINALPLANNEDSCHEDULEDDATE` | DATE |  |  |  |  |
| 184 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 185 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 186 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 187 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 188 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 189 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 190 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 191 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 192 | `USECREATIONUSER` | SMALLINT | NOT NULL |  |  |  |
| 193 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 194 | `CREATIONDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 195 | `CREATIONDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 196 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 197 | `LASTUPDATEDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 198 | `LASTUPDATEDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 199 | `PREVIOUSDESTINATIONORDER` | CHAR(2) |  |  |  |  |
| 200 | `PREVIOUSFULLITEMIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 201 | `MAINTENANCEOFORIGDELIVERY` | SMALLINT | NOT NULL |  |  |  |
| 202 | `KEEPMAINTENANCEORIGDELIVERY` | SMALLINT | NOT NULL |  |  |  |
| 203 | `SUBPROJECTCODE` | DECIMAL(5,0) |  |  |  |  |
| 204 | `SPLITFROMDEMANDCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 205 | `SPLITFROMDEMANDCODE` | CHAR(15) |  |  |  |  |
| 206 | `MQMSPLITREFERENCE` | CHAR(10) |  |  |  |  |
| 207 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 208 | `PROTOTYPEPROJECT` | CHAR(16) |  |  |  |  |
| 209 | `PROTOTYPEVERSION` | CHAR(3) |  |  |  |  |
| 210 | `ORIGINALROUTINGNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 211 | `SAVEORIGINALROUTING` | SMALLINT | NOT NULL |  |  |  |
| 212 | `PREVIOUSROUTINGNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 213 | `ORDERINLATE` | SMALLINT | NOT NULL |  |  |  |
| 214 | `SAVEDINITIALPLANNEDDATE` | DATE |  |  |  |  |
| 215 | `SAVEDFINALPLANNEDDATE` | DATE |  |  |  |  |
| 216 | `CANBEDELETEDBYPLANNING` | SMALLINT | NOT NULL |  |  |  |
| 217 | `CALLEDFROMPLANNING` | SMALLINT | NOT NULL |  |  |  |
| 218 | `DRCODE` | CHAR(8) |  |  |  |  |
| 219 | `DRLINE` | CHAR(15) |  |  |  |  |
| 220 | `ORIGINDRLINENR` | DECIMAL(5,0) |  |  |  |  |
| 221 | `TNAHEADERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 222 | `TNAHEADERCODE` | CHAR(10) |  |  |  |  |
| 223 | `ACTIVITYDATE` | TIMESTAMP |  |  |  |  |
| 224 | `TNASTARTDATE` | TIMESTAMP |  |  |  |  |
| 225 | `TNAENDDATE` | TIMESTAMP |  |  |  |  |
| 226 | `TNARECALCULATIONENDDATE` | TIMESTAMP |  |  |  |  |
| 227 | `TNASTATUS` | INTEGER | NOT NULL |  |  |  |
| 228 | `REALIGNTNA` | SMALLINT | NOT NULL |  |  |  |
| 229 | `GANTTMANAGED` | SMALLINT | NOT NULL |  |  |  |
| 230 | `TNAGANTTRESOURCEREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 231 | `TNAGANTTMARKERREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 232 | `TNAGANTTLINKREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 233 | `TNAGANTTSUBTASKREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 234 | `TNAACTIVITYGANTT` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PRODUCTIONDEMANDBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.PREVIOUSALLOWEDDIVISIONS,
       t.COMPANYCODE,
       t.IMPORTAUTOCOUNTER,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.TEMPLATECODE,
       t.TYPE,
       t.COUNTERCODE,
       t.CODE,
       t.ORDERDATE,
       t.STATISTICALGROUPCODE,
       t.COLLECTIONGROUPCODE
FROM   DB2ADMIN.PRODUCTIONDEMANDBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
