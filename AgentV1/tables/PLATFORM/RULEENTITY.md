# DB2ADMIN.RULEENTITY

- **Module**: `PLATFORM` (low confidence — FK neighbourhood: 1 of 1 related tables are PLATFORM)
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `CODE`
- **FK degree**: referenced by 4 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 31073

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 1 | `LABEL` | CHAR(50) | NOT NULL |  |  |  |
| 2 | `NAME` | CHAR(50) | NOT NULL |  |  |  |
| 3 | `ABSUIXMLPATH` | VARCHAR(50) |  |  |  |  |
| 4 | `ABSUIXMLNAME` | VARCHAR(54) |  |  |  |  |
| 5 | `ADDITIONALDATA` | SMALLINT | NOT NULL |  |  |  |
| 6 | `INPUTUSEDTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 7 | `OUTPUTUSEDTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 8 | `SEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 9 | `FIXEDOUTPUTFIELDS` | SMALLINT | NOT NULL |  |  |  |
| 10 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 11 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 12 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 13 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 14 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 15 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 16 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 4

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `RULEENTITY_ENTITY` | [`INPUTENTITYLIST`](../PLATFORM/INPUTENTITYLIST.md) | `ENTITYCODE` | `INPUTENTITYLIST.ENTITYCODE = RULEENTITY.CODE` |
| `RULEENTITY_ENTITY` | [`OUTPUTENTITYLIST`](../PLATFORM/OUTPUTENTITYLIST.md) | `ENTITYCODE` | `OUTPUTENTITYLIST.ENTITYCODE = RULEENTITY.CODE` |
| `RULEENTITY_ENTITY` | [`RULEENTITYATTRIBUTE`](../LOCALIZATION/RULEENTITYATTRIBUTE.md) | `ENTITYCODE` | `RULEENTITYATTRIBUTE.ENTITYCODE = RULEENTITY.CODE` |
| `RULEENTITY_ENTITY` | [`RULETEMPLATEDETAIL`](../LOCALIZATION/RULETEMPLATEDETAIL.md) | `ENTITYCODE` | `RULETEMPLATEDETAIL.ENTITYCODE = RULEENTITY.CODE` |

## Indexes

- `RULEENTITYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CODE,
       t.LABEL,
       t.NAME,
       t.ABSUIXMLPATH,
       t.ABSUIXMLNAME,
       t.ADDITIONALDATA,
       t.INPUTUSEDTYPE,
       t.OUTPUTUSEDTYPE,
       t.SEQUENCE,
       t.FIXEDOUTPUTFIELDS,
       t.CREATIONDATETIME,
       t.CREATIONUSER
FROM   DB2ADMIN.RULEENTITY t
FETCH FIRST 100 ROWS ONLY;
```
