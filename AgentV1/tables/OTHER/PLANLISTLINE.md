# DB2ADMIN.PLANLISTLINE

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 41
- **Primary key**: `PLANLISTCOMPANYCODE`, `PLANLISTGROUPNUMBER`, `LINE`
- **FK degree**: referenced by 2 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 31625

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PLANLISTCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `PLANLISTGROUPNUMBER` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `LEVELNUMBER` | INTEGER | NOT NULL |  |  |  |
| 4 | `ITEMTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 5 | `ITEMCODE` | VARCHAR(120) |  |  |  |  |
| 6 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 7 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 8 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 9 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 10 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `REQUESTEDWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 17 | `REQUESTEDDELIVERYDATE` | DATE |  |  |  |  |
| 18 | `ORIGINALYREQUIREDPRMQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 19 | `REQUESTEDPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 20 | `ALLOCATEDPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 21 | `AVAILABLEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 22 | `NETREQUIREDPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 23 | `REQUESTEDPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 24 | `EXPLODEDPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 25 | `OCCUPIEDBYOTHERSQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 26 | `ERRORCODE` | CHAR(1) |  |  |  |  |
| 27 | `EXPLOSIONTYPE` | INTEGER | NOT NULL |  |  |  |
| 28 | `HANDLED` | SMALLINT | NOT NULL |  |  |  |
| 29 | `DETAILSLINENUMBER` | INTEGER | NOT NULL |  |  |  |
| 30 | `ORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 31 | `ORDERCODE` | CHAR(15) |  |  |  |  |
| 32 | `RESERVATIONLINE` | DECIMAL(5,0) |  |  |  |  |
| 33 | `CANBENETTEDFROMOTHERS` | SMALLINT | NOT NULL |  |  |  |
| 34 | `ERRORPARAMETERS` | LONG VARCHAR |  |  |  |  |
| 35 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 36 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 37 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 38 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 39 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 40 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PLANLISTLINE.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND PLANLISTLINE.ITEMTYPECODE = ITEMTYPE.CODE` |
| `PLANLIST_PLANLISTLINE` | `PLANLISTCOMPANYCODE`, `PLANLISTGROUPNUMBER` | [`PLANLIST`](../OTHER/PLANLIST.md) | `COMPANYCODE`, `GROUPNUMBER` | RESTRICT | `PLANLISTLINE.PLANLISTCOMPANYCODE = PLANLIST.COMPANYCODE AND PLANLISTLINE.PLANLISTGROUPNUMBER = PLANLIST.GROUPNUMBER` |

## Referenced by (child → this table) — 2

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `PLANLISTLINE_PLANLISTDEMAND` | [`PLANLISTDEMAND`](../OTHER/PLANLISTDEMAND.md) | `PLANLISTLINEPLANLISTCMYCODE`, `PLANLISTLINEPLANLISTGRPNUMBER`, `PLANLISTLINELINE` | `PLANLISTDEMAND.PLANLISTLINEPLANLISTCMYCODE = PLANLISTLINE.PLANLISTCOMPANYCODE AND PLANLISTDEMAND.PLANLISTLINEPLANLISTGRPNUMBER = PLANLISTLINE.PLANLISTGROUPNUMBER AND PLANLISTDEMAND.PLANLISTLINELINE = PLANLISTLINE.LINE` |
| `PLANLISTLINE_PLANLISTREQUISITION` | [`PLANLISTREQUISITION`](../OTHER/PLANLISTREQUISITION.md) | `PLANLISTLINEPLANLISTCMYCODE`, `PLANLISTLINEPLANLISTGRPNUMBER`, `PLANLISTLINELINE` | `PLANLISTREQUISITION.PLANLISTLINEPLANLISTCMYCODE = PLANLISTLINE.PLANLISTCOMPANYCODE AND PLANLISTREQUISITION.PLANLISTLINEPLANLISTGRPNUMBER = PLANLISTLINE.PLANLISTGROUPNUMBER AND PLANLISTREQUISITION.PLANLISTLINELINE = PLANLISTLINE.LINE` |

## Starter query

```sql
SELECT t.PLANLISTCOMPANYCODE,
       t.PLANLISTGROUPNUMBER,
       t.LINE,
       t.LEVELNUMBER,
       t.ITEMTYPECODE,
       t.ITEMCODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06
FROM   DB2ADMIN.PLANLISTLINE t
FETCH FIRST 100 ROWS ONLY;
```
