# DB2ADMIN.BOMCOMPONENTCOMMENT

- **Module**: `ITEM_MASTER` (high confidence — table name starts with 'BOM')
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `BOMCMPBILLOFMATCOMPANYCODE`, `BOMCMPBILLOFMATERIALNUMBERID`, `BOMCOMPONENTSEQUENCE`, `BOMCOMPONENTSUBSEQUENCE`, `ORIGIN`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 5758

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `BOMCMPBILLOFMATCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `BOMCMPBILLOFMATERIALNUMBERID` | DECIMAL(11,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `BOMCOMPONENTSEQUENCE` | DECIMAL(5,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `BOMCOMPONENTSUBSEQUENCE` | DECIMAL(3,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `REPORTTYPE` | CHAR(90) |  |  |  |  |
| 5 | `ORIGIN` | INTEGER | NOT NULL | PK | primary_key |  |
| 6 | `CODE` | CHAR(12) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 7 | `COMMENTTEXT` | LONG VARCHAR | NOT NULL |  |  |  |
| 8 | `COMMENTTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 9 | `CANCELED` | SMALLINT | NOT NULL |  |  |  |
| 10 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 11 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 12 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 13 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 14 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 15 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 16 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `BOMCOMPONENT_COMMENTS` | `BOMCMPBILLOFMATCOMPANYCODE`, `BOMCMPBILLOFMATERIALNUMBERID`, `BOMCOMPONENTSEQUENCE`, `BOMCOMPONENTSUBSEQUENCE` | [`BOMCOMPONENT`](../ITEM_MASTER/BOMCOMPONENT.md) | `BILLOFMATERIALCOMPANYCODE`, `BILLOFMATERIALNUMBERID`, `SEQUENCE`, `SUBSEQUENCE` | RESTRICT | `BOMCOMPONENTCOMMENT.BOMCMPBILLOFMATCOMPANYCODE = BOMCOMPONENT.BILLOFMATERIALCOMPANYCODE AND BOMCOMPONENTCOMMENT.BOMCMPBILLOFMATERIALNUMBERID = BOMCOMPONENT.BILLOFMATERIALNUMBERID AND BOMCOMPONENTCOMMENT.BOMCOMPONENTSEQUENCE = BOMCOMPONENT.SEQUENCE AND BOMCOMPONENTCOMMENT.BOMCOMPONENTSUBSEQUENCE = BOMCOMPONENT.SUBSEQUENCE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `BOMCOMPONENTCOMMENTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.BOMCMPBILLOFMATCOMPANYCODE,
       t.BOMCMPBILLOFMATERIALNUMBERID,
       t.BOMCOMPONENTSEQUENCE,
       t.BOMCOMPONENTSUBSEQUENCE,
       t.REPORTTYPE,
       t.ORIGIN,
       t.CODE,
       t.COMMENTTEXT,
       t.COMMENTTYPE,
       t.CANCELED,
       t.ABSUNIQUEID,
       t.CREATIONDATETIME
FROM   DB2ADMIN.BOMCOMPONENTCOMMENT t
FETCH FIRST 100 ROWS ONLY;
```
