# DB2ADMIN.COSTCENTERBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `COSTING` (high confidence — table name starts with 'COST')
- **Roles**: `staging_mirror`
- **Columns**: 32
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 82721

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 2 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 3 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `CODE` | CHAR(20) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 5 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 6 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 7 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 8 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 9 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 10 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 11 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 12 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 13 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 14 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 15 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 16 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 17 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 18 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 19 | `TRANSLATEDLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 20 | `TRANSLATEDLANGUAGECODE` | CHAR(2) |  |  |  |  |
| 21 | `TRANSLATEDSHORTDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 22 | `PNRESPONSIBLECODE` | CHAR(50) |  |  |  |  |
| 23 | `PNCOSTCENTERTYPE` | INTEGER | NOT NULL |  |  |  |
| 24 | `PNCCCLASSSTANDARDTABLECODE` | CHAR(5) |  |  |  |  |
| 25 | `PNCCCLASSCODE` | CHAR(10) |  |  |  |  |
| 26 | `INITIALDATE` | DATE |  |  |  |  |
| 27 | `FINALDATE` | DATE |  |  |  |  |
| 28 | `INACTIVE` | SMALLINT | NOT NULL |  |  |  |
| 29 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 30 | `PNRESPONSIBLEMANAGER` | CHAR(30) |  |  |  |  |
| 31 | `PNRELEVANTFORPLANNING` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `COSTCENTERBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.WSOPERATION,
       t.IMPORTSTATUS,
       t.IMPCREATIONDATETIME,
       t.IMPCREATIONUSER
FROM   DB2ADMIN.COSTCENTERBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
