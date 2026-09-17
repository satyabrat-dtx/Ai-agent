# DB2ADMIN.DIRECTIVETEMPLATEOUTPUTFIELD

- **Module**: `ITEM_MASTER` (low confidence — FK neighbourhood: 1 of 1 related tables are ITEM_MASTER)
- **Roles**: `business_data`
- **Columns**: 11
- **Primary key**: `DIRECTIVETEMPLATECOMPANYCODE`, `DIRECTIVETEMPLATECODE`, `FIELDNAME`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 199116

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `DIRECTIVETEMPLATECOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `DIRECTIVETEMPLATECODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `FIELDNAME` | CHAR(32) | NOT NULL | PK | primary_key |  |
| 3 | `RESTRICT` | SMALLINT | NOT NULL |  |  |  |
| 4 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 5 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 6 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 7 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 8 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 9 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 10 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `DIRECTIVETEMPLATE_OUTPUTFIELD` | `DIRECTIVETEMPLATECOMPANYCODE`, `DIRECTIVETEMPLATECODE` | [`DIRECTIVETEMPLATE`](../ITEM_MASTER/DIRECTIVETEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `DIRECTIVETEMPLATEOUTPUTFIELD.DIRECTIVETEMPLATECOMPANYCODE = DIRECTIVETEMPLATE.COMPANYCODE AND DIRECTIVETEMPLATEOUTPUTFIELD.DIRECTIVETEMPLATECODE = DIRECTIVETEMPLATE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `DIRECTIVETMPOUTPUTFIELDUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.DIRECTIVETEMPLATECOMPANYCODE,
       t.DIRECTIVETEMPLATECODE,
       t.FIELDNAME,
       t.RESTRICT,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC,
       t.ABSUNIQUEID
FROM   DB2ADMIN.DIRECTIVETEMPLATEOUTPUTFIELD t
FETCH FIRST 100 ROWS ONLY;
```
