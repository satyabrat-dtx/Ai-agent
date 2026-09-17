# DB2ADMIN.CONTAINERDETAIL

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 33
- **Primary key**: `CONTAINERCOMPANYCODE`, `CONTAINERITEMTYPECODE`, `CONTAINERSUBCODE01`, `LINE`, `SUBLINE`
- **FK degree**: referenced by 0 constraint(s), references 5 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 47759

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CONTAINERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `CONTAINERITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `CONTAINERSUBCODE01` | CHAR(20) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `ITEMTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 4 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 5 | `SUBLINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 6 | `DECOSUBCODE01` | CHAR(20) |  |  |  |  |
| 7 | `DECOSUBCODE02` | CHAR(10) |  |  |  |  |
| 8 | `DECOSUBCODE03` | CHAR(10) |  |  |  |  |
| 9 | `DECOSUBCODE04` | CHAR(10) |  |  |  |  |
| 10 | `DECOSUBCODE05` | CHAR(10) |  |  |  |  |
| 11 | `DECOSUBCODE06` | CHAR(10) |  |  |  |  |
| 12 | `DECOSUBCODE07` | CHAR(10) |  |  |  |  |
| 13 | `DECOSUBCODE08` | CHAR(10) |  |  |  |  |
| 14 | `DECOSUBCODE09` | CHAR(10) |  |  |  |  |
| 15 | `DECOSUBCODE10` | CHAR(10) |  |  |  |  |
| 16 | `PRIMARYUOMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 17 | `PRIMARYQUANTITY` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 18 | `INTERNALITEMTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 19 | `INTERNALSUBCODE01` | CHAR(20) |  |  |  |  |
| 20 | `INTERNALSUBCODE02` | CHAR(10) |  |  |  |  |
| 21 | `INTERNALSUBCODE03` | CHAR(10) |  |  |  |  |
| 22 | `INTERNALSUBCODE04` | CHAR(10) |  |  |  |  |
| 23 | `INTERNALSUBCODE05` | CHAR(10) |  |  |  |  |
| 24 | `INTERNALSUBCODE06` | CHAR(10) |  |  |  |  |
| 25 | `INTERNALSUBCODE07` | CHAR(10) |  |  |  |  |
| 26 | `INTERNALSUBCODE08` | CHAR(10) |  |  |  |  |
| 27 | `INTERNALSUBCODE09` | CHAR(10) |  |  |  |  |
| 28 | `INTERNALSUBCODE10` | CHAR(10) |  |  |  |  |
| 29 | `OWNINGCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 30 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 31 | `INTERNALITEMTYPECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 32 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 5

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_OWNINGCOMPANY` | `OWNINGCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `CONTAINERDETAIL.OWNINGCOMPANYCODE = COMPANY.CODE` |
| `CONTAINER_CONTAINERDETAIL` | `CONTAINERCOMPANYCODE`, `CONTAINERITEMTYPECODE`, `CONTAINERSUBCODE01` | [`CONTAINER`](../CORE_MASTER/CONTAINER.md) | `COMPANYCODE`, `ITEMTYPECODE`, `SUBCODE01` | RESTRICT | `CONTAINERDETAIL.CONTAINERCOMPANYCODE = CONTAINER.COMPANYCODE AND CONTAINERDETAIL.CONTAINERITEMTYPECODE = CONTAINER.ITEMTYPECODE AND CONTAINERDETAIL.CONTAINERSUBCODE01 = CONTAINER.SUBCODE01` |
| `ITEMTYPE_INTERNALITEMTYPE` | `INTERNALITEMTYPECOMPANYCODE`, `INTERNALITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `CONTAINERDETAIL.INTERNALITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND CONTAINERDETAIL.INTERNALITEMTYPECODE = ITEMTYPE.CODE` |
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `CONTAINERDETAIL.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND CONTAINERDETAIL.ITEMTYPECODE = ITEMTYPE.CODE` |
| `UNITOFMEASURE_PRIMARYUOM` | `PRIMARYUOMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `CONTAINERDETAIL.PRIMARYUOMCODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `CONTAINERDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CONTAINERCOMPANYCODE,
       t.CONTAINERITEMTYPECODE,
       t.CONTAINERSUBCODE01,
       t.ITEMTYPECODE,
       t.LINE,
       t.SUBLINE,
       t.DECOSUBCODE01,
       t.DECOSUBCODE02,
       t.DECOSUBCODE03,
       t.DECOSUBCODE04,
       t.DECOSUBCODE05,
       t.DECOSUBCODE06
FROM   DB2ADMIN.CONTAINERDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
