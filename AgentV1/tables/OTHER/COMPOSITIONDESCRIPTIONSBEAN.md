# DB2ADMIN.COMPOSITIONDESCRIPTIONSBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 16
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 48919

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `TYPE` | CHAR(1) |  |  |  |  |
| 3 | `DESCRIPTION` | VARCHAR(200) |  |  | description |  |
| 4 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 5 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 6 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 7 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 8 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 9 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 10 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 11 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 12 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 13 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 14 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 15 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **COMPOSITION**.`ABSUNIQUEID` (high confidence — name = 'COMPOSITION' + known child suffix 'DESCRIPTIONS')
  - JOIN predicate: `COMPOSITIONDESCRIPTIONSBEAN.FATHERID = COMPOSITION.ABSUNIQUEID`

## Indexes

- `POSITIONDESCRIPTIONSBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.TYPE,
       t.DESCRIPTION,
       t.WSOPERATION,
       t.IMPORTSTATUS,
       t.IMPCREATIONDATETIME,
       t.IMPCREATIONUSER,
       t.IMPLASTUPDATEDATETIME,
       t.IMPLASTUPDATEUSER,
       t.IMPORTDATETIME,
       t.RETRYNR
FROM   DB2ADMIN.COMPOSITIONDESCRIPTIONSBEAN t
FETCH FIRST 100 ROWS ONLY;
```
