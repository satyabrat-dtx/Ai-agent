# DB2ADMIN.USERGLINKDETAIL

- **Module**: `ITEM_MASTER` (low confidence — FK neighbourhood: 1 of 1 related tables are ITEM_MASTER)
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `USERGLINKUSERGLINKTYPECMYCODE`, `USERGLINKUSERGLINKTYPECODE`, `USERGLINKCODE`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 12159

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `USERGLINKUSERGLINKTYPECMYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `USERGLINKUSERGLINKTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `USERGLINKCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `CODE` | CHAR(10) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 4 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 5 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 6 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 7 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 8 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 9 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 10 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 11 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 12 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 13 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 14 | `OWNINGCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_OWNINGCOMPANY` | `OWNINGCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `USERGLINKDETAIL.OWNINGCOMPANYCODE = COMPANY.CODE` |
| `USERGLINK_DETAIL` | `USERGLINKUSERGLINKTYPECMYCODE`, `USERGLINKUSERGLINKTYPECODE`, `USERGLINKCODE` | [`USERGLINK`](../ITEM_MASTER/USERGLINK.md) | `USERGLINKTYPECOMPANYCODE`, `USERGLINKTYPECODE`, `CODE` | RESTRICT | `USERGLINKDETAIL.USERGLINKUSERGLINKTYPECMYCODE = USERGLINK.USERGLINKTYPECOMPANYCODE AND USERGLINKDETAIL.USERGLINKUSERGLINKTYPECODE = USERGLINK.USERGLINKTYPECODE AND USERGLINKDETAIL.USERGLINKCODE = USERGLINK.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `USERGLINKDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.USERGLINKUSERGLINKTYPECMYCODE,
       t.USERGLINKUSERGLINKTYPECODE,
       t.USERGLINKCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.ABSUNIQUEID
FROM   DB2ADMIN.USERGLINKDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
