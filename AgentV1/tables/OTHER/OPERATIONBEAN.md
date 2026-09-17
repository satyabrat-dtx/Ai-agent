# DB2ADMIN.OPERATIONBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`
- **Columns**: 65
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 47130

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `CODE` | CHAR(8) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 4 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 5 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 6 | `OPERATIONGROUPCODE` | CHAR(10) |  |  |  |  |
| 7 | `EXTERNALRESERVATIONTYPE` | CHAR(2) |  |  |  |  |
| 8 | `PRODRESERVATIONLINKGROUPCODE` | CHAR(20) |  |  |  |  |
| 9 | `LOSSINCREASEMANAGEMENT1` | CHAR(2) |  |  |  |  |
| 10 | `LOSSINCREASETYPE1CODE` | CHAR(3) |  |  |  |  |
| 11 | `LOSSINCREASEMANAGEMENT2` | CHAR(2) |  |  |  |  |
| 12 | `LOSSINCREASETYPE2CODE` | CHAR(3) |  |  |  |  |
| 13 | `LOSSINCREASEMANAGEMENT3` | CHAR(2) |  |  |  |  |
| 14 | `LOSSINCREASETYPE3CODE` | CHAR(3) |  |  |  |  |
| 15 | `LOSSINCREASEMANAGEMENT4` | CHAR(2) |  |  |  |  |
| 16 | `LOSSINCREASETYPE4CODE` | CHAR(3) |  |  |  |  |
| 17 | `LOSSINCREASEMANAGEMENT5` | CHAR(2) |  |  |  |  |
| 18 | `LOSSINCREASETYPE5CODE` | CHAR(3) |  |  |  |  |
| 19 | `LOSSINCREASEMANAGEMENT6` | CHAR(2) |  |  |  |  |
| 20 | `LOSSINCREASETYPE6CODE` | CHAR(3) |  |  |  |  |
| 21 | `LOSSINCREASEMANAGEMENT7` | CHAR(2) |  |  |  |  |
| 22 | `LOSSINCREASETYPE7CODE` | CHAR(3) |  |  |  |  |
| 23 | `LOSSINCREASEMANAGEMENT8` | CHAR(2) |  |  |  |  |
| 24 | `LOSSINCREASETYPE8CODE` | CHAR(3) |  |  |  |  |
| 25 | `TIMEMANAGEMENT1` | CHAR(2) |  |  |  |  |
| 26 | `TIMETYPE1CODE` | CHAR(3) |  |  |  |  |
| 27 | `LINKEDTIME1` | CHAR(2) |  |  |  |  |
| 28 | `SPECIFICUOMTIME1` | SMALLINT | NOT NULL |  |  |  |
| 29 | `TIMEMANAGEMENT2` | CHAR(2) |  |  |  |  |
| 30 | `TIMETYPE2CODE` | CHAR(3) |  |  |  |  |
| 31 | `LINKEDTIME2` | CHAR(2) |  |  |  |  |
| 32 | `SPECIFICUOMTIME2` | SMALLINT | NOT NULL |  |  |  |
| 33 | `TIMEMANAGEMENT3` | CHAR(2) |  |  |  |  |
| 34 | `TIMETYPE3CODE` | CHAR(3) |  |  |  |  |
| 35 | `LINKEDTIME3` | CHAR(2) |  |  |  |  |
| 36 | `SPECIFICUOMTIME3` | SMALLINT | NOT NULL |  |  |  |
| 37 | `TIMEMANAGEMENT4` | CHAR(2) |  |  |  |  |
| 38 | `TIMETYPE4CODE` | CHAR(3) |  |  |  |  |
| 39 | `LINKEDTIME4` | CHAR(2) |  |  |  |  |
| 40 | `SPECIFICUOMTIME4` | SMALLINT | NOT NULL |  |  |  |
| 41 | `TIMEMANAGEMENT5` | CHAR(2) |  |  |  |  |
| 42 | `TIMETYPE5CODE` | CHAR(3) |  |  |  |  |
| 43 | `LINKEDTIME5` | CHAR(2) |  |  |  |  |
| 44 | `SPECIFICUOMTIME5` | SMALLINT | NOT NULL |  |  |  |
| 45 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 46 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 47 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 48 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 49 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 50 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 51 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 52 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 53 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 54 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 55 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 56 | `ENTITYNAME` | CHAR(50) |  |  |  |  |
| 57 | `TRANSLATEDLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 58 | `TRANSLATEDLANGUAGECODE` | CHAR(2) |  |  |  |  |
| 59 | `TRANSLATEDSHORTDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 60 | `HANDLECHILDBUNDLE` | SMALLINT | NOT NULL |  |  |  |
| 61 | `DYELOTHANDLED` | SMALLINT | NOT NULL |  |  |  |
| 62 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 63 | `EXCLUDEFINITECAPACITY` | SMALLINT | NOT NULL |  |  |  |
| 64 | `EXCLUDECHECKOVERCAPACITY` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `OPERATIONBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.OPERATIONGROUPCODE,
       t.EXTERNALRESERVATIONTYPE,
       t.PRODRESERVATIONLINKGROUPCODE,
       t.LOSSINCREASEMANAGEMENT1,
       t.LOSSINCREASETYPE1CODE,
       t.LOSSINCREASEMANAGEMENT2
FROM   DB2ADMIN.OPERATIONBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
