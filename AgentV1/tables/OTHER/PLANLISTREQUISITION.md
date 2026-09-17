# DB2ADMIN.PLANLISTREQUISITION

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 31
- **Primary key**: `PLANLISTLINEPLANLISTCMYCODE`, `PLANLISTLINEPLANLISTGRPNUMBER`, `PLANLISTLINELINE`, `REQUISITIONREQUISITIONTMPCODE`, `REQUISITIONCODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 31687

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PLANLISTLINEPLANLISTCMYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `PLANLISTLINEPLANLISTGRPNUMBER` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `PLANLISTLINELINE` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `LEVELNUMBER` | INTEGER | NOT NULL |  |  |  |
| 4 | `REQUISITIONREQUISITIONTMPCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 5 | `REQUISITIONCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 6 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 7 | `DELIVERYDATE` | DATE |  |  |  |  |
| 8 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 9 | `ITEMCODE` | VARCHAR(120) |  |  |  |  |
| 10 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 11 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 18 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 19 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 20 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 21 | `BASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 22 | `ERRORCODE` | CHAR(1) |  |  |  |  |
| 23 | `USERERRORVALUE` | CHAR(2) |  |  |  |  |
| 24 | `USERERRORTEXT` | CHAR(30) |  |  |  |  |
| 25 | `ERRORPARAMETERS` | LONG VARCHAR |  |  |  |  |
| 26 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 27 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 28 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 29 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 30 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `PLANLISTLINE_PLANLISTREQUISITION` | `PLANLISTLINEPLANLISTCMYCODE`, `PLANLISTLINEPLANLISTGRPNUMBER`, `PLANLISTLINELINE` | [`PLANLISTLINE`](../OTHER/PLANLISTLINE.md) | `PLANLISTCOMPANYCODE`, `PLANLISTGROUPNUMBER`, `LINE` | RESTRICT | `PLANLISTREQUISITION.PLANLISTLINEPLANLISTCMYCODE = PLANLISTLINE.PLANLISTCOMPANYCODE AND PLANLISTREQUISITION.PLANLISTLINEPLANLISTGRPNUMBER = PLANLISTLINE.PLANLISTGROUPNUMBER AND PLANLISTREQUISITION.PLANLISTLINELINE = PLANLISTLINE.LINE` |

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.PLANLISTLINEPLANLISTCMYCODE,
       t.PLANLISTLINEPLANLISTGRPNUMBER,
       t.PLANLISTLINELINE,
       t.LEVELNUMBER,
       t.REQUISITIONREQUISITIONTMPCODE,
       t.REQUISITIONCODE,
       t.WAREHOUSECODE,
       t.DELIVERYDATE,
       t.ITEMTYPECODE,
       t.ITEMCODE,
       t.SUBCODE01,
       t.SUBCODE02
FROM   DB2ADMIN.PLANLISTREQUISITION t
FETCH FIRST 100 ROWS ONLY;
```
