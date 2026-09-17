# DB2ADMIN.GENERALLEDGERACCOUNTBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`
- **Columns**: 86
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 99363

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 3 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 4 | `CODE` | CHAR(10) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 5 | `LONGDESCRIPTION` | VARCHAR(100) |  |  | description | Long human-readable label. |
| 6 | `SHORTDESCRIPTION` | VARCHAR(40) |  |  | description | Short human-readable label. |
| 7 | `SEARCHDESCRIPTION` | VARCHAR(60) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 8 | `ACCOUNTTYPE` | CHAR(1) |  |  |  |  |
| 9 | `ACCOUNTUSAGE` | CHAR(2) |  |  |  |  |
| 10 | `TAXTREATMENT` | CHAR(2) |  |  |  |  |
| 11 | `SECURITYLEVELSYSTEMTABLECODE` | CHAR(5) |  |  |  |  |
| 12 | `SECURITYLEVELCODE` | CHAR(10) |  |  |  |  |
| 13 | `FIRSTUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 14 | `FIRSTUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 15 | `SNDUSERGRPUSERGENGRPTYPECODE` | CHAR(3) |  |  |  |  |
| 16 | `SECONDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 17 | `THIRDUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 18 | `THIRDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 19 | `FOURTHUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 20 | `FOURTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 21 | `FIFTHUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 22 | `FIFTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 23 | `INITIALDATE` | DATE |  |  |  |  |
| 24 | `FINALDATE` | DATE |  |  |  |  |
| 25 | `INACTIVE` | SMALLINT | NOT NULL |  |  |  |
| 26 | `TEXT` | VARCHAR(140) |  |  |  |  |
| 27 | `OPENITEMMAIN` | SMALLINT | NOT NULL |  |  |  |
| 28 | `SALESRELEVANT` | SMALLINT | NOT NULL |  |  |  |
| 29 | `ACCOUNTASSIGNMENTTEXTMANDATORY` | SMALLINT | NOT NULL |  |  |  |
| 30 | `NOFOREIGNCURRENCYVALUATION` | SMALLINT | NOT NULL |  |  |  |
| 31 | `TAXCODECODE` | CHAR(5) |  |  |  |  |
| 32 | `TAXCODEMANDATORY` | SMALLINT | NOT NULL |  |  |  |
| 33 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 34 | `CURRENCYMANDATORY` | SMALLINT | NOT NULL |  |  |  |
| 35 | `ACCOUNTGROUPSTANDARDTABLECODE` | CHAR(5) |  |  |  |  |
| 36 | `ACCOUNTGROUPCODE` | CHAR(10) |  |  |  |  |
| 37 | `INTERESTGROUPSTANDARDTABLECODE` | CHAR(5) |  |  |  |  |
| 38 | `INTERESTGROUPCODE` | CHAR(10) |  |  |  |  |
| 39 | `ADRESSNUMBERNUMBERID` | DECIMAL(8,0) |  |  |  |  |
| 40 | `GROUPACCOUNT` | CHAR(10) |  |  |  |  |
| 41 | `CHECKCODECOSTCENTER` | CHAR(1) |  |  |  |  |
| 42 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 43 | `CHECKCODECOSTUNIT` | CHAR(1) |  |  |  |  |
| 44 | `COSTUNITCODE` | CHAR(20) |  |  |  |  |
| 45 | `CHECKCODEASSET` | CHAR(1) |  |  |  |  |
| 46 | `ASSETCODE` | CHAR(20) |  |  |  |  |
| 47 | `CHECKCODEPROFITCENTER` | CHAR(1) |  |  |  |  |
| 48 | `PROFITCENTERCODE` | CHAR(3) |  |  |  |  |
| 49 | `CHECKCODEWAREHOUSE` | CHAR(1) |  |  |  |  |
| 50 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 51 | `COSTTYPE` | CHAR(1) |  |  |  |  |
| 52 | `COSTTYPEPERC` | INTEGER | NOT NULL |  |  |  |
| 53 | `COSTELEMENTITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 54 | `COSTELEMENTSUBCODE01` | CHAR(20) |  |  |  |  |
| 55 | `BALFIRSTLINEREPORTCODE` | CHAR(3) |  |  |  |  |
| 56 | `BALFIRSTCODE` | CHAR(4) |  |  |  |  |
| 57 | `BALSECONDLINEREPORTCODE` | CHAR(3) |  |  |  |  |
| 58 | `BALSECONDCODE` | CHAR(4) |  |  |  |  |
| 59 | `PLOFIRSTLINEREPORTCODE` | CHAR(3) |  |  |  |  |
| 60 | `PLOFIRSTCODE` | CHAR(4) |  |  |  |  |
| 61 | `PLOSECONDLINEREPORTCODE` | CHAR(3) |  |  |  |  |
| 62 | `PLOSECONDCODE` | CHAR(4) |  |  |  |  |
| 63 | `BABFIRSTLINEREPORTCODE` | CHAR(3) |  |  |  |  |
| 64 | `BABFIRSTCODE` | CHAR(4) |  |  |  |  |
| 65 | `BABSECONDLINEREPORTCODE` | CHAR(3) |  |  |  |  |
| 66 | `BABSECONDCODE` | CHAR(4) |  |  |  |  |
| 67 | `BWAFIRSTLINEREPORTCODE` | CHAR(3) |  |  |  |  |
| 68 | `BWAFIRSTCODE` | CHAR(4) |  |  |  |  |
| 69 | `BWASECONDLINEREPORTCODE` | CHAR(3) |  |  |  |  |
| 70 | `BWASECONDCODE` | CHAR(4) |  |  |  |  |
| 71 | `OTHFIRSTLINEREPORTCODE` | CHAR(3) |  |  |  |  |
| 72 | `OTHFIRSTCODE` | CHAR(4) |  |  |  |  |
| 73 | `OTHSECONDLINEREPORTCODE` | CHAR(3) |  |  |  |  |
| 74 | `OTHSECONDCODE` | CHAR(4) |  |  |  |  |
| 75 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 76 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 77 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 78 | `IMPCREATIONUSER` | CHAR(25) |  |  |  |  |
| 79 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 80 | `IMPLASTUPDATEUSER` | CHAR(25) |  |  |  |  |
| 81 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 82 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 83 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 84 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 85 | `IMPOPERATIONUSER` | CHAR(25) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.IMPORTAUTOCOUNTER,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.ACCOUNTTYPE,
       t.ACCOUNTUSAGE,
       t.TAXTREATMENT,
       t.SECURITYLEVELSYSTEMTABLECODE
FROM   DB2ADMIN.GENERALLEDGERACCOUNTBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
