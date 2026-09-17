# DB2ADMIN.LOGGATEENTRY

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 99
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 146844

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `UGGUSGENGROUPTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 2 | `UGGUSERGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 3 | `UGGCODE` | CHAR(10) |  |  |  |  |
| 4 | `MAINGATEENTRYSRNO` | CHAR(20) | NOT NULL |  |  |  |
| 5 | `GATEENTRYFLAG` | CHAR(2) |  |  |  |  |
| 6 | `MAINGATEENTRYDATE` | DATE | NOT NULL |  |  |  |
| 7 | `COMMINVOICEDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 8 | `COMMINVOICECODE` | CHAR(20) |  |  |  |  |
| 9 | `REPLENISHREQHEADERCODE` | CHAR(15) |  |  |  |  |
| 10 | `EXTOPHEADERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 11 | `EXTOPHEADERCODE` | CHAR(15) |  |  |  |  |
| 12 | `EXTOPLINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 13 | `PURCHASEORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 14 | `PURCHASEORDERCODE` | CHAR(15) |  |  |  |  |
| 15 | `PLANTINVOICEDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 16 | `PLANTINVOICECODE` | CHAR(15) |  |  |  |  |
| 17 | `OUTWARDGATEEMAINGATEENTRYSRNO` | CHAR(20) |  |  |  |  |
| 18 | `SOCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 19 | `SOCODE` | CHAR(15) |  |  |  |  |
| 20 | `IDPROVISIONALCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 21 | `IDPROVISIONALCODE` | CHAR(15) |  |  |  |  |
| 22 | `ORDPRNCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 23 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 24 | `MRNDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 25 | `MRNMRNPREFIXCODE` | CHAR(3) |  |  |  |  |
| 26 | `MRNCODE` | DECIMAL(11,0) |  |  |  |  |
| 27 | `TRANSPORTERINDATETIME` | TIMESTAMP |  |  |  |  |
| 28 | `CHALLANNO` | CHAR(15) |  |  |  |  |
| 29 | `INVOICENO` | CHAR(25) |  |  |  |  |
| 30 | `GATEPASSNO` | CHAR(15) |  |  |  |  |
| 31 | `TRANSPORTEROUTDATETIME` | TIMESTAMP |  |  |  |  |
| 32 | `CHALLANDATE` | DATE |  |  |  |  |
| 33 | `INVOICEDATE` | DATE |  |  |  |  |
| 34 | `GATEPASSDATE` | DATE |  |  |  |  |
| 35 | `DUPLICATEINVFRMTRANSP` | CHAR(1) |  |  |  |  |
| 36 | `TYPEOFVEHICLE` | CHAR(10) |  |  |  |  |
| 37 | `LORRYNO` | CHAR(15) |  |  |  |  |
| 38 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 39 | `TERMSOFSHIPPINGCODE` | CHAR(2) |  |  |  |  |
| 40 | `TRANSPORTERBILLNO` | CHAR(15) |  |  |  |  |
| 41 | `BILLOFENTRYNO` | CHAR(25) |  |  |  |  |
| 42 | `LRNO` | CHAR(15) |  |  |  |  |
| 43 | `DONUMBER` | CHAR(15) |  |  |  |  |
| 44 | `FORMD3NO` | CHAR(15) |  |  |  |  |
| 45 | `TRANSPORTERBILLDATE` | DATE |  |  |  |  |
| 46 | `CARRIERCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 47 | `CARRIERCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 48 | `BILLOFENTRYDATE` | DATE |  |  |  |  |
| 49 | `LRDATE` | DATE |  |  |  |  |
| 50 | `DODATE` | DATE |  |  |  |  |
| 51 | `FORMD3DATE` | DATE |  |  |  |  |
| 52 | `DISPATCHSTATION` | CHAR(15) |  |  |  |  |
| 53 | `WEIGHTACTUAL` | DECIMAL(18,5) |  |  |  |  |
| 54 | `WEIGHTUMCODE` | CHAR(3) |  |  |  |  |
| 55 | `CHARGED` | DECIMAL(18,5) |  |  |  |  |
| 56 | `NOOFPACKAGES` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 57 | `FREIGHTTOPAY` | CHAR(1) |  |  |  |  |
| 58 | `WEIGHTATSPOTGROSS` | DECIMAL(18,5) |  |  |  |  |
| 59 | `WEIGHTNEARUNITGROSS` | DECIMAL(18,5) |  |  |  |  |
| 60 | `WEIGHTATINVOICEGROSS` | DECIMAL(18,5) |  |  |  |  |
| 61 | `WEIGHTATMILLWAREHOUSEGROSS` | DECIMAL(18,5) |  |  |  |  |
| 62 | `WEIGHTATSPOTTARE` | DECIMAL(18,5) |  |  |  |  |
| 63 | `WEIGHTNEARUNITTARE` | DECIMAL(18,5) |  |  |  |  |
| 64 | `WEIGHTATINVOICETARE` | DECIMAL(18,5) |  |  |  |  |
| 65 | `WEIGHTATMILLWAREHOUSETARE` | DECIMAL(18,5) |  |  |  |  |
| 66 | `WEIGHTATSPOTNET` | DECIMAL(18,5) |  |  |  |  |
| 67 | `WEIGHTNEARUNITNET` | DECIMAL(18,5) |  |  |  |  |
| 68 | `WEIGHTATINVOICENET` | DECIMAL(18,5) |  |  |  |  |
| 69 | `WEIGHTATMILLWAREHOUSENET` | DECIMAL(18,5) |  |  |  |  |
| 70 | `RGPNO` | CHAR(15) |  |  |  |  |
| 71 | `JOBWORKCHALLANNO` | CHAR(15) |  |  |  |  |
| 72 | `RGPDATE` | DATE |  |  |  |  |
| 73 | `JOBWORKCHALLANDATE` | DATE |  |  |  |  |
| 74 | `EMPLOYEENAME` | CHAR(35) |  |  |  |  |
| 75 | `REMARK` | VARCHAR(100) |  |  |  |  |
| 76 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 77 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 78 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 79 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 80 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 81 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 82 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 83 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 84 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 85 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 86 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 87 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 88 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 89 | `EXTERNALOPRETURN` | SMALLINT | NOT NULL |  |  |  |
| 90 | `SALDOCPROVISIONALCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 91 | `SALESDOCUMENTPROVISIONALCODE` | CHAR(15) |  |  |  |  |
| 92 | `TERMSOFDELIVERYCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 93 | `TERMSOFSHIPPINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 94 | `MRDMDMRNHEADERDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 95 | `MRDMDMRNHEADERMRNPREFIXCODE` | CHAR(3) |  |  |  |  |
| 96 | `MRDMDMRNHEADERCODE` | DECIMAL(11,0) |  |  |  |  |
| 97 | `MRDMDLINEID` | INTEGER | NOT NULL |  |  |  |
| 98 | `MRDREJECTIONLINEID` | INTEGER | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGGATEENTRY.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.
- child `LOGGATEENTRYDETAIL`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.UGGUSGENGROUPTYPECOMPANYCODE,
       t.UGGUSERGENERICGROUPTYPECODE,
       t.UGGCODE,
       t.MAINGATEENTRYSRNO,
       t.GATEENTRYFLAG,
       t.MAINGATEENTRYDATE,
       t.COMMINVOICEDIVISIONCODE,
       t.COMMINVOICECODE,
       t.REPLENISHREQHEADERCODE,
       t.EXTOPHEADERCOUNTERCODE,
       t.EXTOPHEADERCODE
FROM   DB2ADMIN.LOGGATEENTRY t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
