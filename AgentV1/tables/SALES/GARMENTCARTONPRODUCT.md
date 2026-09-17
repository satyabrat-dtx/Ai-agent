# DB2ADMIN.GARMENTCARTONPRODUCT

- **Module**: `SALES` (low confidence — FK neighbourhood: 1 of 1 related tables are SALES)
- **Roles**: `business_data`
- **Columns**: 29
- **Primary key**: `GARMENTCARTONHEADERCOMPANYCODE`, `GARMENTCARTONHEADERNUMBERID`, `FULLITEMIDENTIFIER`
- **FK degree**: referenced by 1 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 196997

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `GARMENTCARTONHEADERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `GARMENTCARTONHEADERNUMBERID` | DECIMAL(11,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `FULLITEMIDENTIFIER` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 3 | `SALESORDERCOUNTERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 4 | `SALESORDERCODE` | CHAR(15) |  | FK | foreign_key |  |
| 5 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 6 | `ITEMTYPEAFICODE` | CHAR(3) |  | FK | foreign_key |  |
| 7 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 8 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 9 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 10 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `PACKINGGROUP` | CHAR(15) |  |  |  |  |
| 18 | `COLORCODE` | CHAR(10) |  |  |  |  |
| 19 | `SIZECODE` | CHAR(10) |  |  |  |  |
| 20 | `TOTALQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 21 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 22 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 23 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 24 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 25 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 26 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 27 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 28 | `LINKEDSIZECODE` | CHAR(10) |  |  |  |  |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `GARMENTCARTONHEADER_CHILDCARTONPRODUCT` | `GARMENTCARTONHEADERCOMPANYCODE`, `GARMENTCARTONHEADERNUMBERID` | [`GARMENTCARTONHEADER`](../CORE_MASTER/GARMENTCARTONHEADER.md) | `COMPANYCODE`, `NUMBERID` | RESTRICT | `GARMENTCARTONPRODUCT.GARMENTCARTONHEADERCOMPANYCODE = GARMENTCARTONHEADER.COMPANYCODE AND GARMENTCARTONPRODUCT.GARMENTCARTONHEADERNUMBERID = GARMENTCARTONHEADER.NUMBERID` |
| `ITEMTYPE_ITEMTYPEAFI` | `ITEMTYPEAFICOMPANYCODE`, `ITEMTYPEAFICODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `GARMENTCARTONPRODUCT.ITEMTYPEAFICOMPANYCODE = ITEMTYPE.COMPANYCODE AND GARMENTCARTONPRODUCT.ITEMTYPEAFICODE = ITEMTYPE.CODE` |
| `SALESORDER_SALESORDER` | `GARMENTCARTONHEADERCOMPANYCODE`, `SALESORDERCOUNTERCODE`, `SALESORDERCODE` | [`SALESORDER`](../SALES/SALESORDER.md) | `COMPANYCODE`, `COUNTERCODE`, `CODE` | RESTRICT | `GARMENTCARTONPRODUCT.GARMENTCARTONHEADERCOMPANYCODE = SALESORDER.COMPANYCODE AND GARMENTCARTONPRODUCT.SALESORDERCOUNTERCODE = SALESORDER.COUNTERCODE AND GARMENTCARTONPRODUCT.SALESORDERCODE = SALESORDER.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `GARMENTCARTONPRODUCT_CHILDTRANSACTION` | [`GARMENTCARTONTRANSACTION`](../INVENTORY/GARMENTCARTONTRANSACTION.md) | `GMTCRTPRDGMTCRTHDRCOMPANYCODE`, `GMTCRTPRDGMTCRTHEADERNUMBERID`, `GMTCRTPRDFULLITEMIDENTIFIER` | `GARMENTCARTONTRANSACTION.GMTCRTPRDGMTCRTHDRCOMPANYCODE = GARMENTCARTONPRODUCT.GARMENTCARTONHEADERCOMPANYCODE AND GARMENTCARTONTRANSACTION.GMTCRTPRDGMTCRTHEADERNUMBERID = GARMENTCARTONPRODUCT.GARMENTCARTONHEADERNUMBERID AND GARMENTCARTONTRANSACTION.GMTCRTPRDFULLITEMIDENTIFIER = GARMENTCARTONPRODUCT.FULLITEMIDENTIFIER` |

## Indexes

- `GARMENTCARTONPRODUCTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.GARMENTCARTONHEADERCOMPANYCODE,
       t.GARMENTCARTONHEADERNUMBERID,
       t.FULLITEMIDENTIFIER,
       t.SALESORDERCOUNTERCODE,
       t.SALESORDERCODE,
       t.ITEMTYPEAFICOMPANYCODE,
       t.ITEMTYPEAFICODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05
FROM   DB2ADMIN.GARMENTCARTONPRODUCT t
FETCH FIRST 100 ROWS ONLY;
```
