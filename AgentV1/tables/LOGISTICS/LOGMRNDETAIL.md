# DB2ADMIN.LOGMRNDETAIL

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 136
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 133152

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `MRNHEADERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `MRNHEADERDIVISIONCODE` | CHAR(3) | NOT NULL |  |  |  |
| 2 | `MRNHEADERMRNPREFIXCODE` | CHAR(3) | NOT NULL |  |  |  |
| 3 | `MRNHEADERCODE` | DECIMAL(11,0) | NOT NULL |  |  |  |
| 4 | `LINEID` | INTEGER | NOT NULL |  |  |  |
| 5 | `TRANSACTIONNUMBER` | CHAR(15) | NOT NULL |  |  |  |
| 6 | `PURORDERCOUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 7 | `PURCHASEORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 8 | `PURCHASEORDERCODE` | CHAR(15) |  |  |  |  |
| 9 | `ORDERLINE` | DECIMAL(7,0) | NOT NULL |  |  |  |
| 10 | `ORDERSUBLINE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 11 | `TARIFFCODE` | CHAR(20) |  |  |  |  |
| 12 | `INPUTCAPITAL` | INTEGER | NOT NULL |  |  |  |
| 13 | `INVOICEQUANTITY` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 14 | `RECEIVEDQUANTITY` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 15 | `SHORTAGEOREXCESSQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 16 | `REJECTEDQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 17 | `DAMAGEDQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 18 | `ACCEPTEDQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 19 | `TAXTEMPLATETEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 20 | `TAXTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 21 | `UNITPRICE` | DECIMAL(18,5) |  |  |  |  |
| 22 | `TERMSOFPAYMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 23 | `TERMSOFPAYMENTCODE` | CHAR(3) |  |  |  |  |
| 24 | `MODEOFPAYMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 25 | `MODEOFPAYMENTCODE` | CHAR(3) |  |  |  |  |
| 26 | `DUPLICATEINVFRMTRANSP` | CHAR(1) |  |  |  |  |
| 27 | `TERMSOFDELIVERYCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 28 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 29 | `TYPEOFVEHICLE` | CHAR(10) |  |  |  |  |
| 30 | `LORRYNO` | CHAR(15) |  |  |  |  |
| 31 | `TERMSOFSHIPPINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 32 | `TERMSOFSHIPPINGCODE` | CHAR(2) |  |  |  |  |
| 33 | `TRANSPORTERBILLNO` | CHAR(15) |  |  |  |  |
| 34 | `BILLOFENTRYNO` | CHAR(25) |  |  |  |  |
| 35 | `LRNO` | CHAR(15) |  |  |  |  |
| 36 | `FORMD3NO` | CHAR(15) |  |  |  |  |
| 37 | `DISPATCHSTATION` | CHAR(15) |  |  |  |  |
| 38 | `TRANSPORTERBILLDATE` | DATE |  |  |  |  |
| 39 | `CARRIERCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 40 | `CARRIERCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 41 | `BILLOFENTRYDATE` | DATE |  |  |  |  |
| 42 | `LRDATE` | DATE |  |  |  |  |
| 43 | `FORMD3DATE` | DATE |  |  |  |  |
| 44 | `DEPARTMENTCODE` | CHAR(8) |  |  |  |  |
| 45 | `WEIGHTACTUAL` | DECIMAL(18,5) |  |  |  |  |
| 46 | `NOOFPACKAGES` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 47 | `FREIGHTTOPAY` | CHAR(1) |  |  |  |  |
| 48 | `COSTCENTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 49 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 50 | `WEIGHTCHARGED` | DECIMAL(18,5) |  |  |  |  |
| 51 | `BILLPASSEDAMT` | DECIMAL(18,5) |  |  |  |  |
| 52 | `DEDUCTIONAMT` | DECIMAL(18,5) |  |  |  |  |
| 53 | `REMARK` | VARCHAR(100) |  |  |  |  |
| 54 | `REMARK1` | CHAR(10) |  |  |  |  |
| 55 | `REMARK2` | CHAR(10) |  |  |  |  |
| 56 | `REMARK3` | CHAR(10) |  |  |  |  |
| 57 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 58 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 59 | `EXTOPCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 60 | `EXTOPCODE` | CHAR(15) |  |  |  |  |
| 61 | `EXTOPORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 62 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 63 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 64 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 65 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 66 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 67 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 68 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 69 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 70 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 71 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 72 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 73 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 74 | `PRIMARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 75 | `SECONDARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 76 | `PACKINGQTY` | DECIMAL(15,5) |  |  |  |  |
| 77 | `PRIMARYUMCODE` | CHAR(3) |  |  |  |  |
| 78 | `SECONDARYUMCODE` | CHAR(3) |  |  |  |  |
| 79 | `PACKINGUMCODE` | CHAR(3) |  |  |  |  |
| 80 | `BASEPRIMARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 81 | `BASESECONDARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 82 | `BASEPRIMARYUMCODE` | CHAR(3) |  |  |  |  |
| 83 | `BASESECONDARYUMCODE` | CHAR(3) |  |  |  |  |
| 84 | `LOGICALWAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 85 | `LOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 86 | `BASICVALUE` | DECIMAL(18,5) |  |  |  |  |
| 87 | `GROSSVALUEWOHEADER` | DECIMAL(18,5) |  |  |  |  |
| 88 | `GROSSVALUE` | DECIMAL(18,5) |  |  |  |  |
| 89 | `BASICVALUECC` | DECIMAL(18,5) |  |  |  |  |
| 90 | `GROSSVALUEWOHEADERCC` | DECIMAL(18,5) |  |  |  |  |
| 91 | `GROSSVALUECC` | DECIMAL(18,5) |  |  |  |  |
| 92 | `RG23PART1AEXCISEYEARREGNO` | CHAR(30) |  |  |  |  |
| 93 | `RG23PART1AEXCISEYEARCODE` | CHAR(4) |  |  |  |  |
| 94 | `RG23PART1ACODE` | CHAR(15) |  |  |  |  |
| 95 | `RG23PART1CEXCISEYEARREGNO` | CHAR(30) |  |  |  |  |
| 96 | `RG23PART1CEXCISEYEARCODE` | CHAR(4) |  |  |  |  |
| 97 | `RG23PART1CCODE` | CHAR(15) |  |  |  |  |
| 98 | `SAMPLEMETER` | DECIMAL(15,5) |  |  |  |  |
| 99 | `WASTAGEMETER` | DECIMAL(15,5) |  |  |  |  |
| 100 | `SHORTAGEMETER` | DECIMAL(15,5) |  |  |  |  |
| 101 | `EXCESSMETER` | DECIMAL(15,5) |  |  |  |  |
| 102 | `ACTUALQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 103 | `AGRADE` | DECIMAL(15,5) |  |  |  |  |
| 104 | `BGRADE` | DECIMAL(15,5) |  |  |  |  |
| 105 | `CGRADE` | DECIMAL(15,5) |  |  |  |  |
| 106 | `FRESH` | DECIMAL(15,5) |  |  |  |  |
| 107 | `SCHEMETYPECODE` | CHAR(3) |  |  |  |  |
| 108 | `ADVLICENCECODE` | CHAR(30) |  |  |  |  |
| 109 | `ALAPPLICATIONDATE` | DATE |  |  |  |  |
| 110 | `ADVANCELICENSENO` | CHAR(15) |  |  |  |  |
| 111 | `ADVANCELICENSEDATE` | DATE |  |  |  |  |
| 112 | `EPCGAPPLNEPCGAPPLICATIONCODE` | CHAR(30) |  |  |  |  |
| 113 | `EPCGAPPLICATIONDATE` | DATE |  |  |  |  |
| 114 | `EPCGLICENSENO` | CHAR(30) |  |  |  |  |
| 115 | `EPCGLICENSEDATE` | DATE |  |  |  |  |
| 116 | `CUSTOMINVOICECODE` | CHAR(20) |  |  |  |  |
| 117 | `PLANTINVOICECODE` | CHAR(15) |  |  |  |  |
| 118 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 119 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 120 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 121 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 122 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 123 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 124 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 125 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 126 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 127 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 128 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 129 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 130 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 131 | `REJECTIONVALUE` | DECIMAL(18,5) |  |  |  |  |
| 132 | `INTERPILPLNINVOICECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 133 | `INTERPILPLNINVDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 134 | `INTERPILPLANTINVOICECODE` | CHAR(15) |  |  |  |  |
| 135 | `INTERPILINVOICELINENO` | DECIMAL(3,0) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGMRNDETAIL.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.MRNHEADERCOMPANYCODE,
       t.MRNHEADERDIVISIONCODE,
       t.MRNHEADERMRNPREFIXCODE,
       t.MRNHEADERCODE,
       t.LINEID,
       t.TRANSACTIONNUMBER,
       t.PURORDERCOUNTERCOMPANYCODE,
       t.PURCHASEORDERCOUNTERCODE,
       t.PURCHASEORDERCODE,
       t.ORDERLINE,
       t.ORDERSUBLINE,
       t.TARIFFCODE
FROM   DB2ADMIN.LOGMRNDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
