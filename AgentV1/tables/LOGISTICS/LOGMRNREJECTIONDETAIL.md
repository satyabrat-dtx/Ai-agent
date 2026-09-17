# DB2ADMIN.LOGMRNREJECTIONDETAIL

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 96
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 221054

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CODE` | CHAR(12) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 1 | `MDMRNHEADERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 2 | `MDMRNHEADERDIVISIONCODE` | CHAR(3) | NOT NULL |  |  |  |
| 3 | `MDMRNHEADERMRNPREFIXCODE` | CHAR(3) | NOT NULL |  |  |  |
| 4 | `MDMRNHEADERCODE` | DECIMAL(11,0) | NOT NULL |  |  |  |
| 5 | `MDLINEID` | INTEGER | NOT NULL |  |  |  |
| 6 | `REJECTIONLINEID` | INTEGER | NOT NULL |  |  |  |
| 7 | `TRANSACTIONNUMBER` | CHAR(15) | NOT NULL |  |  |  |
| 8 | `PURORDERCOUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 9 | `PURCHASEORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 10 | `PURCHASEORDERCODE` | CHAR(15) |  |  |  |  |
| 11 | `ORDERLINE` | DECIMAL(7,0) | NOT NULL |  |  |  |
| 12 | `ORDERSUBLINE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 13 | `ORDPRNCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 14 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 15 | `LOGICALWAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 16 | `LOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 17 | `PLANTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 18 | `PLANTCODE` | CHAR(8) |  |  |  |  |
| 19 | `INTERNALDOCUMENTNUMBER` | INTEGER | NOT NULL |  |  |  |
| 20 | `INPUTCAPITAL` | INTEGER | NOT NULL |  |  |  |
| 21 | `TARIFFCODE` | CHAR(20) |  |  |  |  |
| 22 | `INVOICEQUANTITY` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 23 | `RECEIVEDQUANTITY` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 24 | `SHORTAGEOREXCESSQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 25 | `REJECTEDQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 26 | `REJECTEDSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 27 | `REJECTEDPACKINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 28 | `DAMAGEDQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 29 | `ACCEPTEDQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 30 | `TAXTEMPLATETEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 31 | `TAXTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 32 | `UNITPRICE` | DECIMAL(18,5) |  |  |  |  |
| 33 | `TERMSOFPAYMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 34 | `TERMSOFPAYMENTCODE` | CHAR(3) |  |  |  |  |
| 35 | `MODEOFPAYMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 36 | `MODEOFPAYMENTCODE` | CHAR(3) |  |  |  |  |
| 37 | `DUPLICATEINVFRMTRANSP` | CHAR(1) |  |  |  |  |
| 38 | `TERMSOFDELIVERYCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 39 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 40 | `TYPEOFVEHICLE` | CHAR(10) |  |  |  |  |
| 41 | `LORRYNO` | CHAR(15) |  |  |  |  |
| 42 | `TRANSPORTERBILLNO` | CHAR(15) |  |  |  |  |
| 43 | `TERMSOFSHIPPINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 44 | `TERMSOFSHIPPINGCODE` | CHAR(2) |  |  |  |  |
| 45 | `BILLOFENTRYNO` | CHAR(15) |  |  |  |  |
| 46 | `LRNO` | CHAR(15) |  |  |  |  |
| 47 | `FORMD3NO` | CHAR(15) |  |  |  |  |
| 48 | `DISPATCHSTATION` | CHAR(15) |  |  |  |  |
| 49 | `TRANSACTIONDATE` | DATE |  |  |  |  |
| 50 | `TRANSPORTERBILLDATE` | DATE |  |  |  |  |
| 51 | `CARRIERCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 52 | `CARRIERCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 53 | `BILLOFENTRYDATE` | DATE |  |  |  |  |
| 54 | `LRDATE` | DATE |  |  |  |  |
| 55 | `FORMD3DATE` | DATE |  |  |  |  |
| 56 | `DEPARTMENTCODE` | CHAR(8) |  |  |  |  |
| 57 | `WEIGHTACTUAL` | DECIMAL(18,5) |  |  |  |  |
| 58 | `NOOFPACKAGES` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 59 | `FREIGHTTOPAY` | CHAR(1) |  |  |  |  |
| 60 | `COSTCENTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 61 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 62 | `WEIGHTCHARGED` | DECIMAL(18,5) |  |  |  |  |
| 63 | `BILLPASSEDAMT` | DECIMAL(18,5) |  |  |  |  |
| 64 | `DEDUCTIONAMT` | DECIMAL(18,5) |  |  |  |  |
| 65 | `REMARK` | VARCHAR(100) |  |  |  |  |
| 66 | `BASICVALUE` | DECIMAL(18,5) |  |  |  |  |
| 67 | `GROSSVALUEWOHEADER` | DECIMAL(18,5) |  |  |  |  |
| 68 | `GROSSVALUE` | DECIMAL(18,5) |  |  |  |  |
| 69 | `BASICVALUECC` | DECIMAL(18,5) |  |  |  |  |
| 70 | `GROSSVALUEWOHEADERCC` | DECIMAL(18,5) |  |  |  |  |
| 71 | `GROSSVALUECC` | DECIMAL(18,5) |  |  |  |  |
| 72 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 73 | `FLAG` | CHAR(15) |  |  |  |  |
| 74 | `SAPMESSAGE` | LONG VARCHAR |  |  |  |  |
| 75 | `FINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 76 | `FINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 77 | `FINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 78 | `FINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 79 | `FINDOCCODE` | CHAR(15) |  |  |  |  |
| 80 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 81 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 82 | `OTHFINDOCCODE` | CHAR(15) |  |  |  |  |
| 83 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 84 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 85 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 86 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 87 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 88 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 89 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 90 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 91 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 92 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 93 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 94 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 95 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGMRNREJECTIONDETAIL.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.CODE,
       t.MDMRNHEADERCOMPANYCODE,
       t.MDMRNHEADERDIVISIONCODE,
       t.MDMRNHEADERMRNPREFIXCODE,
       t.MDMRNHEADERCODE,
       t.MDLINEID,
       t.REJECTIONLINEID,
       t.TRANSACTIONNUMBER,
       t.PURORDERCOUNTERCOMPANYCODE,
       t.PURCHASEORDERCOUNTERCODE,
       t.PURCHASEORDERCODE,
       t.ORDERLINE
FROM   DB2ADMIN.LOGMRNREJECTIONDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
