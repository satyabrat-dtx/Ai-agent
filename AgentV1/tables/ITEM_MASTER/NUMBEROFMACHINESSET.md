# DB2ADMIN.NUMBEROFMACHINESSET

- **Module**: `ITEM_MASTER` (low confidence — FK neighbourhood: 1 of 1 related tables are ITEM_MASTER)
- **Roles**: `business_data`
- **Columns**: 9
- **Primary key**: `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE`, `CODE`
- **FK degree**: referenced by 2 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 210874

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 1 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 4 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 5 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 6 | `UNITOFMEASURECODE` | CHAR(3) |  | FK | foreign_key |  |
| 7 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 8 | `OWNINGCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_OWNINGCOMPANY` | `OWNINGCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `NUMBEROFMACHINESSET.OWNINGCOMPANYCODE = COMPANY.CODE` |
| `UNITOFMEASURE_UNITOFMEASURE` | `UNITOFMEASURECODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `NUMBEROFMACHINESSET.UNITOFMEASURECODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 2

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `NUMBEROFMACHINESSET_NUMBEROFMACHINESQUANTITIES` | [`NUMBEROFMACHINESQUANTITIES`](../ITEM_MASTER/NUMBEROFMACHINESQUANTITIES.md) | `COMPANYCODE`, `ITEMTYPECODE`, `CODE` | `NUMBEROFMACHINESQUANTITIES.COMPANYCODE = NUMBEROFMACHINESSET.ITEMTYPECOMPANYCODE AND NUMBEROFMACHINESQUANTITIES.ITEMTYPECODE = NUMBEROFMACHINESSET.ITEMTYPECODE AND NUMBEROFMACHINESQUANTITIES.CODE = NUMBEROFMACHINESSET.CODE` |
| `NUMBEROFMACHINESSET_NUMBEROFMACHINESSET` | [`PRODUCTWORKCENTERANDOPERATTR`](../ITEM_MASTER/PRODUCTWORKCENTERANDOPERATTR.md) | `ITCOMPANYCODE`, `ITEMTYPECODE`, `CODE` | `PRODUCTWORKCENTERANDOPERATTR.ITCOMPANYCODE = NUMBEROFMACHINESSET.ITEMTYPECOMPANYCODE AND PRODUCTWORKCENTERANDOPERATTR.ITEMTYPECODE = NUMBEROFMACHINESSET.ITEMTYPECODE AND PRODUCTWORKCENTERANDOPERATTR.CODE = NUMBEROFMACHINESSET.CODE` |

## Indexes

- `NUMBEROFMACHINESSETUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.UNITOFMEASURECODE,
       t.ABSUNIQUEID,
       t.OWNINGCOMPANYCODE
FROM   DB2ADMIN.NUMBEROFMACHINESSET t
FETCH FIRST 100 ROWS ONLY;
```
