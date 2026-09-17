# DB2ADMIN.LOGMRNHEADER

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 159
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 133511

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL |  |  | Division within a company; second-level organisational discriminator. |
| 2 | `MRNPREFIXCODE` | CHAR(3) | NOT NULL |  |  |  |
| 3 | `CODE` | DECIMAL(11,0) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 4 | `MRNDATE` | DATE | NOT NULL |  |  |  |
| 5 | `PURCHASEORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 6 | `PURCHASEORDERCODE` | CHAR(15) |  |  |  |  |
| 7 | `PLANTINVOICEDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 8 | `PLANTINVOICECODE` | CHAR(15) |  |  |  |  |
| 9 | `ORDPRNCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 10 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 11 | `CHALLANNO` | CHAR(15) |  |  |  |  |
| 12 | `INVOICENO` | CHAR(25) |  |  |  |  |
| 13 | `MAINGATEENTRYSRNO` | CHAR(15) |  |  |  |  |
| 14 | `GATEPASSNO` | CHAR(15) |  |  |  |  |
| 15 | `PRESSMARKNO` | CHAR(5) |  |  |  |  |
| 16 | `DONUMBER` | CHAR(15) |  |  |  |  |
| 17 | `CHALLANDATE` | DATE |  |  |  |  |
| 18 | `INVOICEDATE` | DATE |  |  |  |  |
| 19 | `MAINGATEENTRYDATE` | DATE |  |  |  |  |
| 20 | `GATEPASSDATE` | DATE |  |  |  |  |
| 21 | `PRESSNO` | CHAR(15) |  |  |  |  |
| 22 | `DODATE` | DATE |  |  |  |  |
| 23 | `DUPLICATEINVFRMTRANSP` | CHAR(1) |  |  |  |  |
| 24 | `TERMSOFDELIVERYCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 25 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 26 | `TYPEOFVEHICLE` | CHAR(10) |  |  |  |  |
| 27 | `LORRYNO` | CHAR(15) |  |  |  |  |
| 28 | `TRANSPORTERBILLNO` | CHAR(15) |  |  |  |  |
| 29 | `TERMSOFSHIPPINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 30 | `TERMSOFSHIPPINGCODE` | CHAR(2) |  |  |  |  |
| 31 | `BILLOFENTRYNO` | CHAR(25) |  |  |  |  |
| 32 | `LRNO` | CHAR(15) |  |  |  |  |
| 33 | `FORMD3NO` | CHAR(15) |  |  |  |  |
| 34 | `DISPATCHSTATION` | CHAR(15) |  |  |  |  |
| 35 | `TRANSPORTERBILLDATE` | DATE |  |  |  |  |
| 36 | `CARRIERCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 37 | `CARRIERCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 38 | `BILLOFENTRYDATE` | DATE |  |  |  |  |
| 39 | `LRDATE` | DATE |  |  |  |  |
| 40 | `FORMD3DATE` | DATE |  |  |  |  |
| 41 | `WEIGHTACTUAL` | DECIMAL(18,5) |  |  |  |  |
| 42 | `CHARGED` | DECIMAL(18,5) |  |  |  |  |
| 43 | `NOOFPACKAGES` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 44 | `FREIGHTTOPAY` | CHAR(1) |  |  |  |  |
| 45 | `WEIGHTATSPOTGROSS` | DECIMAL(18,5) |  |  |  |  |
| 46 | `WEIGHTNEARUNITGROSS` | DECIMAL(18,5) |  |  |  |  |
| 47 | `WEIGHTATINVOICEGROSS` | DECIMAL(18,5) |  |  |  |  |
| 48 | `WEIGHTATMILLWAREHOUSEGROSS` | DECIMAL(18,5) |  |  |  |  |
| 49 | `WEIGHTATSPOTTARE` | DECIMAL(18,5) |  |  |  |  |
| 50 | `WEIGHTNEARUNITTARE` | DECIMAL(18,5) |  |  |  |  |
| 51 | `WEIGHTATINVOICETARE` | DECIMAL(18,5) |  |  |  |  |
| 52 | `WEIGHTATMILLWAREHOUSETARE` | DECIMAL(18,5) |  |  |  |  |
| 53 | `WEIGHTATSPOTNET` | DECIMAL(18,5) |  |  |  |  |
| 54 | `WEIGHTNEARUNITNET` | DECIMAL(18,5) |  |  |  |  |
| 55 | `WEIGHTATINVOICENET` | DECIMAL(18,5) |  |  |  |  |
| 56 | `WEIGHTATMILLWAREHOUSENET` | DECIMAL(18,5) |  |  |  |  |
| 57 | `TAXTEMPLATETEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 58 | `TAXTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 59 | `TERMSOFPAYMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 60 | `TERMSOFPAYMENTCODE` | CHAR(3) |  |  |  |  |
| 61 | `MODEOFPAYMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 62 | `MODEOFPAYMENTCODE` | CHAR(3) |  |  |  |  |
| 63 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 64 | `EXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 65 | `TDSTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 66 | `RG23PART2AEXCISEYEARREGNO` | CHAR(30) |  |  |  |  |
| 67 | `RG23PART2AEXCISEYEARCODE` | CHAR(4) |  |  |  |  |
| 68 | `RG23PART2ACODE` | CHAR(15) |  |  |  |  |
| 69 | `OURAR3NO` | CHAR(15) |  |  |  |  |
| 70 | `RG23PART2CEXCISEYEARREGNO` | CHAR(30) |  |  |  |  |
| 71 | `RG23PART2CEXCISEYEARCODE` | CHAR(4) |  |  |  |  |
| 72 | `RG23PART2CCODE` | CHAR(15) |  |  |  |  |
| 73 | `SUPPLIERAR3NO` | CHAR(15) |  |  |  |  |
| 74 | `AR4NO` | CHAR(15) |  |  |  |  |
| 75 | `TRANSITBONDNO` | CHAR(15) |  |  |  |  |
| 76 | `OURINVNO` | CHAR(15) |  |  |  |  |
| 77 | `RGPNO` | CHAR(15) |  |  |  |  |
| 78 | `JOBWORKCHALLANNO` | CHAR(15) |  |  |  |  |
| 79 | `OURAR3DATE` | DATE |  |  |  |  |
| 80 | `SUPPLIERAR3DATE` | DATE |  |  |  |  |
| 81 | `AR4DATE` | DATE |  |  |  |  |
| 82 | `TRANSITBONDDATE` | DATE |  |  |  |  |
| 83 | `OURINVDATE` | DATE |  |  |  |  |
| 84 | `RGPDATE` | DATE |  |  |  |  |
| 85 | `JOBWORKCHALLANDATE` | DATE |  |  |  |  |
| 86 | `DEPARTMENTCODE` | CHAR(8) |  |  |  |  |
| 87 | `COSTCENTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 88 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 89 | `AGENTCODE` | CHAR(3) |  |  |  |  |
| 90 | `BROKERCODE` | CHAR(3) |  |  |  |  |
| 91 | `CONTRACTORCODE` | CHAR(3) |  |  |  |  |
| 92 | `EMPLOYEENAME` | CHAR(35) |  |  |  |  |
| 93 | `REMARK` | VARCHAR(100) |  |  |  |  |
| 94 | `CREDITTOEMPLOYEE` | DECIMAL(18,5) |  |  |  |  |
| 95 | `CREDITTOSUPPLIER` | DECIMAL(18,5) |  |  |  |  |
| 96 | `CREDITTOANOTHERSUPPLIER` | DECIMAL(18,5) |  |  |  |  |
| 97 | `BILLPASSEDAMT` | DECIMAL(18,5) |  |  |  |  |
| 98 | `DEDUCTIONAMT` | DECIMAL(18,5) |  |  |  |  |
| 99 | `BASICVALUE` | DECIMAL(18,5) |  |  |  |  |
| 100 | `GROSSVALUE` | DECIMAL(18,5) |  |  |  |  |
| 101 | `ROUNDOFFVALUE` | DECIMAL(18,5) |  |  |  |  |
| 102 | `NETVALUE` | DECIMAL(18,5) |  |  |  |  |
| 103 | `NETPAYABLE` | DECIMAL(18,5) |  |  |  |  |
| 104 | `DEDUCTIONAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 105 | `BASICVALUECC` | DECIMAL(18,5) |  |  |  |  |
| 106 | `GROSSVALUECC` | DECIMAL(18,5) |  |  |  |  |
| 107 | `ROUNDOFFVALUECC` | DECIMAL(18,5) |  |  |  |  |
| 108 | `NETVALUECC` | DECIMAL(18,5) |  |  |  |  |
| 109 | `INVOICEAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 110 | `EXPENSEAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 111 | `ROUNDOFFITAXCODE` | CHAR(3) |  |  |  |  |
| 112 | `CONFIRMEDFLAG` | INTEGER | NOT NULL |  |  |  |
| 113 | `EXCISEDUTY` | INTEGER | NOT NULL |  |  |  |
| 114 | `PURCHASEINVOICECODE` | CHAR(25) |  |  |  |  |
| 115 | `PURCHASEINVOICEINVOICEDATE` | DATE |  |  |  |  |
| 116 | `USEDCOUNTER` | INTEGER | NOT NULL |  |  |  |
| 117 | `POSTINGFLAG` | INTEGER | NOT NULL |  |  |  |
| 118 | `STEP` | CHAR(1) |  |  |  |  |
| 119 | `SCHEMETYPECODE` | CHAR(3) |  |  |  |  |
| 120 | `ALCODE` | CHAR(30) |  |  |  |  |
| 121 | `ALAPPLICATIONDATE` | DATE |  |  |  |  |
| 122 | `ADVANCELICENSENO` | CHAR(15) |  |  |  |  |
| 123 | `ADVANCELICENSEDATE` | DATE |  |  |  |  |
| 124 | `DEPBAPPCODE` | CHAR(12) |  |  |  |  |
| 125 | `DEPBDATE` | DATE |  |  |  |  |
| 126 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 127 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 128 | `FLAG` | CHAR(15) |  |  |  |  |
| 129 | `SAPMESSAGE` | LONG VARCHAR |  |  |  |  |
| 130 | `FINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 131 | `FINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 132 | `FINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 133 | `FINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 134 | `FINDOCCODE` | CHAR(15) |  |  |  |  |
| 135 | `DFINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 136 | `DFINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 137 | `DFINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 138 | `DFINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 139 | `DFINDOCCODE` | CHAR(15) |  |  |  |  |
| 140 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 141 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 142 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 143 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 144 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 145 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 146 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 147 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 148 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 149 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 150 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 151 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 152 | `OTHFINDOCCODE` | CHAR(15) |  |  |  |  |
| 153 | `OTHFINDOCCODE2` | CHAR(15) |  |  |  |  |
| 154 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 155 | `INTERPICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 156 | `INTERPIDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 157 | `INTERPICODE` | CHAR(15) |  |  |  |  |
| 158 | `PURINVORDPRNCSMSUPPLIERTYPE` | CHAR(1) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGMRNHEADER.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.MRNPREFIXCODE,
       t.CODE,
       t.MRNDATE,
       t.PURCHASEORDERCOUNTERCODE,
       t.PURCHASEORDERCODE,
       t.PLANTINVOICEDIVISIONCODE,
       t.PLANTINVOICECODE,
       t.ORDPRNCUSTOMERSUPPLIERTYPE,
       t.ORDPRNCUSTOMERSUPPLIERCODE,
       t.CHALLANNO
FROM   DB2ADMIN.LOGMRNHEADER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
