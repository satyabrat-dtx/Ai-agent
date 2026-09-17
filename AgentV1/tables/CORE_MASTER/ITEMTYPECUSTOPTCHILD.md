# DB2ADMIN.ITEMTYPECUSTOPTCHILD

- **Module**: `CORE_MASTER` (high confidence — table name starts with 'ITEMTYPE')
- **Roles**: `business_data`
- **Columns**: 19
- **Primary key**: `ITCMP`, `ITCODE`, `ITEMTYPECMPCODE`
- **FK degree**: referenced by 0 constraint(s), references 6 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 45560

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ITCMP` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `ITCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `ITEMTYPECMPCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `RESWHSCODE` | CHAR(8) |  | FK | foreign_key |  |
| 4 | `RULECODE` | CHAR(10) |  | FK | foreign_key |  |
| 5 | `ITEMTYPECMPCOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 6 | `RESWHSCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 7 | `BOMNATURE` | CHAR(1) | NOT NULL |  |  |  |
| 8 | `CALCULATEQTYCODE` | CHAR(20) |  |  |  |  |
| 9 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 10 | `ASSEMBLYUOMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 11 | `COSTCENTERCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 12 | `COSTCENTERCODE` | CHAR(20) |  | FK | foreign_key |  |
| 13 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 14 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 15 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 16 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 17 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 18 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 6

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COSTCENTER_COSTCENTER` | `COSTCENTERCOMPANYCODE`, `COSTCENTERCODE` | [`COSTCENTER`](../COSTING/COSTCENTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ITEMTYPECUSTOPTCHILD.COSTCENTERCOMPANYCODE = COSTCENTER.COMPANYCODE AND ITEMTYPECUSTOPTCHILD.COSTCENTERCODE = COSTCENTER.CODE` |
| `ITEMTYPECUSTOMIZEDOPTIONS_CMPS` | `ITCMP`, `ITCODE` | [`ITEMTYPECUSTOMIZEDOPTIONS`](../CORE_MASTER/ITEMTYPECUSTOMIZEDOPTIONS.md) | `COMPANYCODE`, `ITEMTYPECODE` | RESTRICT | `ITEMTYPECUSTOPTCHILD.ITCMP = ITEMTYPECUSTOMIZEDOPTIONS.COMPANYCODE AND ITEMTYPECUSTOPTCHILD.ITCODE = ITEMTYPECUSTOMIZEDOPTIONS.ITEMTYPECODE` |
| `ITEMTYPE_ITEMTYPECMP` | `ITEMTYPECMPCOMPANYCODE`, `ITEMTYPECMPCODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ITEMTYPECUSTOPTCHILD.ITEMTYPECMPCOMPANYCODE = ITEMTYPE.COMPANYCODE AND ITEMTYPECUSTOPTCHILD.ITEMTYPECMPCODE = ITEMTYPE.CODE` |
| `LOGICALWAREHOUSE_RESWHS` | `RESWHSCOMPANYCODE`, `RESWHSCODE` | [`LOGICALWAREHOUSE`](../WAREHOUSE/LOGICALWAREHOUSE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ITEMTYPECUSTOPTCHILD.RESWHSCOMPANYCODE = LOGICALWAREHOUSE.COMPANYCODE AND ITEMTYPECUSTOPTCHILD.RESWHSCODE = LOGICALWAREHOUSE.CODE` |
| `RULES_RULE` | `ITCMP`, `RULECODE` | [`RULES`](../CORE_MASTER/RULES.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ITEMTYPECUSTOPTCHILD.ITCMP = RULES.COMPANYCODE AND ITEMTYPECUSTOPTCHILD.RULECODE = RULES.CODE` |
| `UNITOFMEASURE_ASSEMBLYUOM` | `ASSEMBLYUOMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `ITEMTYPECUSTOPTCHILD.ASSEMBLYUOMCODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ITEMTYPECUSTOPTCHILDUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ITCMP,
       t.ITCODE,
       t.ITEMTYPECMPCODE,
       t.RESWHSCODE,
       t.RULECODE,
       t.ITEMTYPECMPCOMPANYCODE,
       t.RESWHSCOMPANYCODE,
       t.BOMNATURE,
       t.CALCULATEQTYCODE,
       t.ABSUNIQUEID,
       t.ASSEMBLYUOMCODE,
       t.COSTCENTERCOMPANYCODE
FROM   DB2ADMIN.ITEMTYPECUSTOPTCHILD t
FETCH FIRST 100 ROWS ONLY;
```
