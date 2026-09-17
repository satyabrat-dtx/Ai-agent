# DB2ADMIN.LOGFINEXPNEGOTIATION

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 136
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 202528

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(10) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `BUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 3 | `NEGOTIATIONDATE` | DATE |  |  |  |  |
| 4 | `BILLOFEXCHANGEDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 5 | `BILLOFEXCHANGECODE` | CHAR(12) |  |  |  |  |
| 6 | `NEGOTIATIONTYPE` | CHAR(1) |  |  |  |  |
| 7 | `NEGOTIATEDVALUE` | DECIMAL(18,5) |  |  |  |  |
| 8 | `AGENCYCOMMISSIONRATE` | DECIMAL(18,5) |  |  |  |  |
| 9 | `AGENCYCOMMISSIONVALUE` | DECIMAL(18,5) |  |  |  |  |
| 10 | `AGENTCODE` | CHAR(3) |  |  |  |  |
| 11 | `AGENTGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 12 | `AGENTGLCODE` | CHAR(20) |  |  |  |  |
| 13 | `COLLECTIONVALUE` | DECIMAL(18,5) |  |  |  |  |
| 14 | `TOTALVALUE` | DECIMAL(18,5) |  |  |  |  |
| 15 | `REALISEDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 16 | `RUNMANUALCLOSURE` | SMALLINT | NOT NULL |  |  |  |
| 17 | `PCGLACCOUNTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 18 | `PCGLACCOUNTCODE` | CHAR(20) |  |  |  |  |
| 19 | `POSTINGDATE` | DATE |  |  |  |  |
| 20 | `DOCUMENTCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 21 | `MADEOF` | CHAR(1) |  |  |  |  |
| 22 | `DISCOUNTGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 23 | `DISCOUNTGLCODE` | CHAR(20) |  |  |  |  |
| 24 | `DSCSUPCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 25 | `DSCSUPCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 26 | `STATUS` | CHAR(1) |  |  |  |  |
| 27 | `BANKCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 28 | `BANKCODE` | CHAR(20) |  |  |  |  |
| 29 | `REFERENCEDATE` | DATE |  |  |  |  |
| 30 | `DUEDATE` | DATE |  |  |  |  |
| 31 | `NOOFDAYS` | INTEGER | NOT NULL |  |  |  |
| 32 | `PROFITCENTERPROFITCENTERCODE` | CHAR(10) |  |  |  |  |
| 33 | `COSTCENTERCOSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 34 | `CUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 35 | `CUSTOMERCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 36 | `SPOTRATE` | DECIMAL(18,5) |  |  |  |  |
| 37 | `MARKETVALUE` | DECIMAL(18,5) |  |  |  |  |
| 38 | `INVOICEDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 39 | `INVOICECODE` | CHAR(20) |  |  |  |  |
| 40 | `INVOICECURRENCYCODE` | CHAR(4) |  |  |  |  |
| 41 | `INVOICEDATE` | DATE |  |  |  |  |
| 42 | `INVOICEVALUE` | DECIMAL(18,5) |  |  |  |  |
| 43 | `REFERENCENUM` | CHAR(20) |  |  |  |  |
| 44 | `NOOFDAYSCHARGED` | DECIMAL(3,0) |  |  |  |  |
| 45 | `INTERESTRATE` | DECIMAL(5,2) |  |  |  |  |
| 46 | `NOOFDAYSCHARGEDNXT` | DECIMAL(3,0) |  |  |  |  |
| 47 | `INTERESTRATENXT` | DECIMAL(5,2) |  |  |  |  |
| 48 | `SHIPMENTDATE` | DATE |  |  |  |  |
| 49 | `PAYMENTMETHODCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 50 | `PAYMENTMETHODCODE` | CHAR(3) |  |  |  |  |
| 51 | `CALCULTEDINTEREST` | DECIMAL(18,5) |  |  |  |  |
| 52 | `CALCULTEDCOMMISSION` | DECIMAL(18,5) |  |  |  |  |
| 53 | `CALCULTEDPOSTAGE` | DECIMAL(18,5) |  |  |  |  |
| 54 | `CALCULTEDSTAMP` | DECIMAL(18,5) |  |  |  |  |
| 55 | `MANUALINTEREST` | DECIMAL(18,5) |  |  |  |  |
| 56 | `MANUALCOMMISSION` | DECIMAL(18,5) |  |  |  |  |
| 57 | `MANUALPOSTAGE` | DECIMAL(18,5) |  |  |  |  |
| 58 | `MANUALSTAMP` | DECIMAL(18,5) |  |  |  |  |
| 59 | `GAINORLOSSGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 60 | `GAINORLOSSGLCODE` | CHAR(20) |  |  |  |  |
| 61 | `GAINORLOSSAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 62 | `FIRSTGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 63 | `FIRSTGLCODE` | CHAR(20) |  |  |  |  |
| 64 | `SECONDGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 65 | `SECONDGLCODE` | CHAR(20) |  |  |  |  |
| 66 | `THIRDGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 67 | `THIRDGLCODE` | CHAR(20) |  |  |  |  |
| 68 | `FOURTHGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 69 | `FOURTHGLCODE` | CHAR(20) |  |  |  |  |
| 70 | `COLLECTIONREFERENCENO` | CHAR(15) |  |  |  |  |
| 71 | `COLLECTIONREFDATE` | DATE |  |  |  |  |
| 72 | `REALISATIONDATE` | DATE |  |  |  |  |
| 73 | `COLLECTIONCHARGES` | DECIMAL(18,5) |  |  |  |  |
| 74 | `COLLECTIONCHARGESMAUAL` | DECIMAL(18,5) |  |  |  |  |
| 75 | `OTHERCHARGES` | DECIMAL(18,5) |  |  |  |  |
| 76 | `OTHERCHARGESMAUAL` | DECIMAL(18,5) |  |  |  |  |
| 77 | `PCADJUSTEDVALUE` | DECIMAL(18,5) |  |  |  |  |
| 78 | `CCVALUE` | DECIMAL(18,5) |  |  |  |  |
| 79 | `FIFTHGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 80 | `FIFTHGLCODE` | CHAR(20) |  |  |  |  |
| 81 | `EDCVALUE` | DECIMAL(18,5) |  |  |  |  |
| 82 | `SIXTHGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 83 | `SIXTHGLCODE` | CHAR(20) |  |  |  |  |
| 84 | `SEVENTHGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 85 | `SEVENTHGLCODE` | CHAR(20) |  |  |  |  |
| 86 | `ACCEPTANCEDATE` | DATE |  |  |  |  |
| 87 | `DISCREPENCY` | CHAR(1) |  |  |  |  |
| 88 | `COMMENTS` | VARCHAR(500) |  |  |  |  |
| 89 | `CGSTVALUE` | DECIMAL(18,5) |  |  |  |  |
| 90 | `SGSTVALUE` | DECIMAL(18,5) |  |  |  |  |
| 91 | `CGSTGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 92 | `CGSTGLCODE` | CHAR(20) |  |  |  |  |
| 93 | `SGSTGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 94 | `SGSTGLCODE` | CHAR(20) |  |  |  |  |
| 95 | `FINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 96 | `FINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 97 | `FINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 98 | `FINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 99 | `FINDOCCODE` | CHAR(15) |  |  |  |  |
| 100 | `REMARK` | VARCHAR(255) |  |  |  |  |
| 101 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 102 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 103 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 104 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 105 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 106 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 107 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 108 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 109 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 110 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 111 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 112 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 113 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 114 | `EXCHANGERATE` | DECIMAL(18,5) |  |  |  |  |
| 115 | `HELDFORCLAIMPCLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 116 | `HELDFORCLAIMPCLCODE` | CHAR(20) |  |  |  |  |
| 117 | `HELDFORCLAIMFDBNCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 118 | `HELDFORCLAIMFDBNCODE` | CHAR(20) |  |  |  |  |
| 119 | `HELDFORCLAIMINDC` | DECIMAL(18,5) |  |  |  |  |
| 120 | `HELDFORCLAIMINCC` | DECIMAL(18,5) |  |  |  |  |
| 121 | `BILLAMOUNTFCVALUE` | DECIMAL(18,5) |  |  |  |  |
| 122 | `ADVANCENO` | CHAR(15) |  |  |  |  |
| 123 | `ADVANCEDATE` | DATE |  |  |  |  |
| 124 | `LOANSANCTIONEDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 125 | `COLADVGLACCOUNTCODECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 126 | `COLADVGLACCOUNTCODECODE` | CHAR(20) |  |  |  |  |
| 127 | `UNPAIDVALUE` | DECIMAL(18,5) |  |  |  |  |
| 128 | `CURRENTADJUSTMENT` | DECIMAL(18,5) |  |  |  |  |
| 129 | `REMARKS` | VARCHAR(255) |  |  |  |  |
| 130 | `PCGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 131 | `PCGLCODE` | CHAR(20) |  |  |  |  |
| 132 | `INTERESTCHARGES2COMPANYCODE` | CHAR(3) |  |  |  |  |
| 133 | `INTERESTCHARGES2CODE` | CHAR(20) |  |  |  |  |
| 134 | `INTEREST2` | DECIMAL(18,5) |  |  |  |  |
| 135 | `PCADJUSTEDVALUEFORINR` | DECIMAL(18,5) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFINEXPNEGOTIATION.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.
- child `LOGFINEXPNEGOTIATIONADVANCE`.`FATHERID` → this table's `ABSUNIQUEID` (medium confidence)
- child `LOGFINEXPNEGOTIATIONINVOICE`.`FATHERID` → this table's `ABSUNIQUEID` (medium confidence)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.BUSINESSUNITCODE,
       t.NEGOTIATIONDATE,
       t.BILLOFEXCHANGEDIVISIONCODE,
       t.BILLOFEXCHANGECODE,
       t.NEGOTIATIONTYPE,
       t.NEGOTIATEDVALUE,
       t.AGENCYCOMMISSIONRATE,
       t.AGENCYCOMMISSIONVALUE,
       t.AGENTCODE,
       t.AGENTGLCOMPANYCODE
FROM   DB2ADMIN.LOGFINEXPNEGOTIATION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
