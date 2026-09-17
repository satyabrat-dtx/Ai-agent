# DB2ADMIN.BOMCOMPONENTRULEBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `ITEM_MASTER` (high confidence — table name starts with 'BOM')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 17
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 213906

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `SEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 3 | `RULECODE` | CHAR(10) |  |  |  |  |
| 4 | `FROMQUICKRULE` | SMALLINT | NOT NULL |  |  |  |
| 5 | `RULEUSABILITY` | INTEGER | NOT NULL |  |  |  |
| 6 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 7 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 8 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 9 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 10 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 11 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 12 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 13 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 14 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 15 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 16 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **BOMCOMPONENT**.`ABSUNIQUEID` (medium confidence — name = 'BOMCOMPONENT' + recurring fragment 'RULE' (seen in 40 tables))
  - JOIN predicate: `BOMCOMPONENTRULEBEAN.FATHERID = BOMCOMPONENT.ABSUNIQUEID`

## Indexes

- `BOMCOMPONENTRULEBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.SEQUENCE,
       t.RULECODE,
       t.FROMQUICKRULE,
       t.RULEUSABILITY,
       t.WSOPERATION,
       t.IMPOPERATIONUSER,
       t.IMPORTSTATUS,
       t.IMPCREATIONDATETIME,
       t.IMPCREATIONUSER,
       t.IMPLASTUPDATEDATETIME
FROM   DB2ADMIN.BOMCOMPONENTRULEBEAN t
FETCH FIRST 100 ROWS ONLY;
```
