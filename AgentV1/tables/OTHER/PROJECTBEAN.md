# DB2ADMIN.PROJECTBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`
- **Columns**: 53
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 206979

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 3 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 4 | `CODE` | CHAR(20) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 5 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 6 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 7 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 8 | `CUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 9 | `CUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 10 | `BUDGETMANAGED` | SMALLINT | NOT NULL |  |  |  |
| 11 | `BUDGETPROGRESSSTATUS` | INTEGER | NOT NULL |  |  |  |
| 12 | `BUDGETSTATUS` | CHAR(1) |  |  |  |  |
| 13 | `PROJECTBUDGETBYPLANNINGRUN` | INTEGER | NOT NULL |  |  |  |
| 14 | `BUDGETTOBEUPDONPLANNINGRUN` | SMALLINT | NOT NULL |  |  |  |
| 15 | `BUDGETRUNAPPROVE` | SMALLINT | NOT NULL |  |  |  |
| 16 | `BUDGETAPPROVALDATE` | DATE |  |  |  |  |
| 17 | `BUDGETAPPROVALUSER` | CHAR(50) |  |  |  |  |
| 18 | `BUDGETRUNUNAPPROVE` | SMALLINT | NOT NULL |  |  |  |
| 19 | `BUDGETUNAPPROVALDATE` | DATE |  |  |  |  |
| 20 | `BUDGETUNAPPROVALUSER` | CHAR(50) |  |  |  |  |
| 21 | `PLANNERANNOTATION` | VARCHAR(250) |  |  |  |  |
| 22 | `PLANRUNNING` | SMALLINT | NOT NULL |  |  |  |
| 23 | `CANBEEXPLODED` | SMALLINT | NOT NULL |  |  |  |
| 24 | `PLANNINGTEMPLATECODE` | CHAR(8) |  |  |  |  |
| 25 | `PROGRESSSTATUS` | INTEGER | NOT NULL |  |  |  |
| 26 | `LINESCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 27 | `ERRORS` | VARCHAR(960) |  |  |  |  |
| 28 | `WARNINGS` | VARCHAR(960) |  |  |  |  |
| 29 | `TRACECREATIONID` | DECIMAL(11,0) |  |  |  |  |
| 30 | `TRACELINE` | INTEGER | NOT NULL |  |  |  |
| 31 | `SUBMITTEDJOBJOBNUMBER` | BIGINT | NOT NULL |  |  |  |
| 32 | `TRANSLATEDLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 33 | `TRANSLATEDLANGUAGECODE` | CHAR(2) |  |  |  |  |
| 34 | `TRANSLATEDSHORTDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 35 | `WFMSTATUS` | INTEGER | NOT NULL |  |  |  |
| 36 | `EXISTSBUDGETDETAIL` | SMALLINT | NOT NULL |  |  |  |
| 37 | `OWNINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 38 | `WFMPISTATUS` | INTEGER | NOT NULL |  |  |  |
| 39 | `WFMSTATUSREASONCODE` | CHAR(50) |  |  |  |  |
| 40 | `WFMREMARK` | CLOB(2000000) |  |  |  |  |
| 41 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 42 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 43 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 44 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 45 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 46 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 47 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 48 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 49 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 50 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 51 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 52 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PROJECTBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

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
       t.CUSTOMERTYPE,
       t.CUSTOMERCODE,
       t.BUDGETMANAGED,
       t.BUDGETPROGRESSSTATUS
FROM   DB2ADMIN.PROJECTBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
