# DB2ADMIN.SALESORDERDELIVERYTORELEASE

- **Module**: `SALES` (high confidence — table name starts with 'SALESORDER')
- **Roles**: `business_data`
- **Columns**: 82
- **Primary key**: `CREATIONNUMBER`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 73184

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONNUMBER` | BIGINT | NOT NULL | PK | primary_key |  |
| 1 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 2 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `DLVSALORDLINESALORDCNTCODE` | CHAR(8) |  |  |  |  |
| 5 | `DLVSALORDERLINESALESORDERCODE` | CHAR(15) |  |  |  |  |
| 6 | `DLVSALESORDERLINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 7 | `DLVSALESORDERLINEORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 8 | `DLVSALORDLINECMPORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 9 | `DELIVERYDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 10 | `LINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 11 | `OUTOFCREDIT` | SMALLINT | NOT NULL |  |  |  |
| 12 | `CREDITCHECKFORCED` | SMALLINT | NOT NULL |  |  |  |
| 13 | `RELEASETYPE` | CHAR(2) | NOT NULL |  |  |  |
| 14 | `RELEASEPRIORITY` | INTEGER | NOT NULL |  |  |  |
| 15 | `DELIVERYDATE` | DATE |  |  |  |  |
| 16 | `CONFIRMEDDELIVERYDATE` | DATE |  |  |  |  |
| 17 | `ERRORCODE` | CHAR(12) | NOT NULL |  |  |  |
| 18 | `STATUS` | CHAR(1) | NOT NULL |  |  |  |
| 19 | `RELEASELINECODE` | CHAR(15) |  |  |  |  |
| 20 | `RELEASELINELINE` | DECIMAL(7,0) |  |  |  |  |
| 21 | `RELEASELINESUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 22 | `RELEASELINECMPRELEASELINE` | DECIMAL(3,0) |  |  |  |  |
| 23 | `ORDPRNCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 24 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 25 | `ORDERPARTNERDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 26 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 27 | `ITEMNATURE` | CHAR(1) | NOT NULL |  |  |  |
| 28 | `SUBCODE01` | CHAR(20) | NOT NULL |  | generic_classification_code |  |
| 29 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 30 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 31 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 32 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 33 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 34 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 35 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 36 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 37 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 38 | `ITEMCODE` | VARCHAR(120) |  |  |  |  |
| 39 | `ITEMDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 40 | `QUALITYCODE` | DECIMAL(2,0) |  |  |  |  |
| 41 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 42 | `RELEASEUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 43 | `RELEASEUSERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 44 | `RELEASEBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 45 | `RELEASEBASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 46 | `RELEASEUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 47 | `RELEASEUSERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 48 | `RELEASEBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 49 | `RELEASEBASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 50 | `RELEASEUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 51 | `RELEASEUSERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 52 | `RESIDUALUSERQUANTITY` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 53 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 54 | `AMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 55 | `RESIDUALAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 56 | `ONLYBYAMOUNT` | SMALLINT | NOT NULL |  |  |  |
| 57 | `SHPQTYGREATERDELIVERYDETAIL` | SMALLINT | NOT NULL |  |  |  |
| 58 | `PARTIALSHIPPING` | SMALLINT | NOT NULL |  |  |  |
| 59 | `RELEASEONLYAVAILABLE` | SMALLINT | NOT NULL |  |  |  |
| 60 | `AVAILABILITYWAREHOUSEGROUPCODE` | CHAR(3) |  |  |  |  |
| 61 | `FROMALLOCATIONSPLIT` | SMALLINT | NOT NULL |  |  |  |
| 62 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 63 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 64 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 65 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 66 | `WAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 67 | `AVLWAREHOUSEGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 68 | `STATISTICALGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 69 | `CONSIDERBASEQUANTITIES` | SMALLINT | NOT NULL |  |  |  |
| 70 | `ALCCODE` | CHAR(15) |  |  |  |  |
| 71 | `TRANSLATEDITEMDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 72 | `ALCLINENUMBER` | DECIMAL(5,0) |  |  |  |  |
| 73 | `ALCCOMPONENTLINENUMBER` | DECIMAL(5,0) |  |  |  |  |
| 74 | `SHIPPEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 75 | `SHIPPEDBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 76 | `SHIPPEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 77 | `SHIPPEDBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 78 | `SHIPPEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 79 | `EXISTSOVERDUEAMOUNT` | SMALLINT | NOT NULL |  |  |  |
| 80 | `OVERDUEAMOUNTFORCED` | SMALLINT | NOT NULL |  |  |  |
| 81 | `OVERDUEAMOUNT` | DECIMAL(18,5) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SALORDERDELIVERYTORELEASEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONNUMBER,
       t.CREATIONUSER,
       t.LINE,
       t.COMPANYCODE,
       t.DLVSALORDLINESALORDCNTCODE,
       t.DLVSALORDERLINESALESORDERCODE,
       t.DLVSALESORDERLINEORDERLINE,
       t.DLVSALESORDERLINEORDERSUBLINE,
       t.DLVSALORDLINECMPORDERLINE,
       t.DELIVERYDELIVERYLINE,
       t.LINETEMPLATECODE,
       t.OUTOFCREDIT
FROM   DB2ADMIN.SALESORDERDELIVERYTORELEASE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
