# DB2ADMIN.GLMASTERBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`
- **Columns**: 30
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 147689

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `CODE` | CHAR(20) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 4 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 5 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 6 | `GLTYPE` | CHAR(1) |  |  |  |  |
| 7 | `BSPLFLAG` | CHAR(1) |  |  |  |  |
| 8 | `CHARTOFACCUSGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 9 | `CHARTOFACCOUNTCODE` | CHAR(10) |  |  |  |  |
| 10 | `STATUS` | CHAR(1) |  |  |  |  |
| 11 | `RECONCILATIONFLAG` | SMALLINT | NOT NULL |  |  |  |
| 12 | `BANKCASHFLAG` | CHAR(1) |  |  |  |  |
| 13 | `FACLASSIFICATIONTYPE` | CHAR(1) |  |  |  |  |
| 14 | `APPFORFOREX` | SMALLINT | NOT NULL |  |  |  |
| 15 | `OWNINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 16 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 17 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 18 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 19 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 20 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 21 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 22 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 23 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 24 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 25 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 26 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 27 | `GLCLEARINGFLAG` | SMALLINT | NOT NULL |  |  |  |
| 28 | `BLOCKDIRECTENTRYALLOWED` | SMALLINT | NOT NULL |  |  |  |
| 29 | `ENTITYNAME` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `GLMASTERBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.GLTYPE,
       t.BSPLFLAG,
       t.CHARTOFACCUSGENGROUPTYPECODE,
       t.CHARTOFACCOUNTCODE,
       t.STATUS,
       t.RECONCILATIONFLAG
FROM   DB2ADMIN.GLMASTERBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
