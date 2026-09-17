# DB2ADMIN.RULEBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`
- **Columns**: 22
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 212382

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `CODE` | CHAR(10) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `RULETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 4 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 5 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 6 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 7 | `TRANSLATEDLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 8 | `TRANSLATEDLANGUAGECODE` | CHAR(2) |  |  |  |  |
| 9 | `TRANSLATEDSHORTDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 10 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 11 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 12 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 13 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 14 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 15 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 16 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 17 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 18 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 19 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 20 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 21 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `RULEBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.CODE,
       t.RULETEMPLATECODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.TRANSLATEDLONGDESCRIPTION,
       t.TRANSLATEDLANGUAGECODE,
       t.TRANSLATEDSHORTDESCRIPTION,
       t.WSOPERATION,
       t.IMPOPERATIONUSER
FROM   DB2ADMIN.RULEBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
