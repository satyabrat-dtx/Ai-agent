# DB2ADMIN.USERGLINK

- **Module**: `ITEM_MASTER` (low confidence — FK neighbourhood: 1 of 1 related tables are ITEM_MASTER)
- **Roles**: `business_data`
- **Columns**: 14
- **Primary key**: `USERGLINKTYPECOMPANYCODE`, `USERGLINKTYPECODE`, `CODE`
- **FK degree**: referenced by 1 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 8376

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `USERGLINKTYPECOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `USERGLINKTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `CODE` | CHAR(10) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 4 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 5 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 6 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 7 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 8 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 9 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 10 | `OWNINGCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 11 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 12 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 13 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_OWNINGCOMPANY` | `OWNINGCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `USERGLINK.OWNINGCOMPANYCODE = COMPANY.CODE` |
| `USERGLINKTYPE_GROUP` | `USERGLINKTYPECOMPANYCODE`, `USERGLINKTYPECODE` | [`USERGLINKTYPE`](../ITEM_MASTER/USERGLINKTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `USERGLINK.USERGLINKTYPECOMPANYCODE = USERGLINKTYPE.COMPANYCODE AND USERGLINK.USERGLINKTYPECODE = USERGLINKTYPE.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `USERGLINK_DETAIL` | [`USERGLINKDETAIL`](../ITEM_MASTER/USERGLINKDETAIL.md) | `USERGLINKUSERGLINKTYPECMYCODE`, `USERGLINKUSERGLINKTYPECODE`, `USERGLINKCODE` | `USERGLINKDETAIL.USERGLINKUSERGLINKTYPECMYCODE = USERGLINK.USERGLINKTYPECOMPANYCODE AND USERGLINKDETAIL.USERGLINKUSERGLINKTYPECODE = USERGLINK.USERGLINKTYPECODE AND USERGLINKDETAIL.USERGLINKCODE = USERGLINK.CODE` |

## Indexes

- `USERGLINKUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.USERGLINKTYPECOMPANYCODE,
       t.USERGLINKTYPECODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.OWNINGCOMPANYCODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.USERGLINK t
FETCH FIRST 100 ROWS ONLY;
```
