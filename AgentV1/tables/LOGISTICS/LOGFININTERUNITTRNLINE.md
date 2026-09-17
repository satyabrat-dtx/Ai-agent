# DB2ADMIN.LOGFININTERUNITTRNLINE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 81
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 223923

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FININTERUNITTRNCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `FININTERUNITTRANSACTIONCODE` | CHAR(15) | NOT NULL |  |  |  |
| 2 | `LINENO` | INTEGER | NOT NULL |  |  |  |
| 3 | `ODLBUSINESSUNITCODE` | CHAR(10) | NOT NULL |  |  |  |
| 4 | `ODLFINANCIALYEARCODE` | DECIMAL(4,0) | NOT NULL |  |  |  |
| 5 | `ODLDOCUMENTTEMPLATECODE` | CHAR(3) | NOT NULL |  |  |  |
| 6 | `ODLSTATISTICALGROUPCODE` | CHAR(6) | NOT NULL |  |  |  |
| 7 | `ODLCODE` | CHAR(15) | NOT NULL |  |  |  |
| 8 | `ODLLINENUMBER` | DECIMAL(7,0) | NOT NULL |  |  |  |
| 9 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 10 | `EXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 11 | `AMOUNTTOCLEAR` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 12 | `GAINLOSS` | DECIMAL(18,5) |  |  |  |  |
| 13 | `ORDERPARTNERTYPE` | CHAR(1) |  |  |  |  |
| 14 | `ORDERPARTNERCODE` | CHAR(8) |  |  |  |  |
| 15 | `OPTDSTDSTEUGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 16 | `OPTDSTDSTYPECODE` | CHAR(10) |  |  |  |  |
| 17 | `OPTDSTDSCODE` | CHAR(6) |  |  |  |  |
| 18 | `OPTDSTDSITAXCODE` | CHAR(3) |  |  |  |  |
| 19 | `OPTDSEXEMPTIONFROMDATE` | DATE |  |  |  |  |
| 20 | `DSTBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 21 | `DSTFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 22 | `DSTDOCUMENTTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 23 | `DSTSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 24 | `DSTCODE` | CHAR(15) |  |  |  |  |
| 25 | `DSTLINENUMBER` | DECIMAL(7,0) |  |  |  |  |
| 26 | `TDSPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 27 | `TDSAPPLICABLEAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 28 | `TDSAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 29 | `TDSGLCODE` | CHAR(20) |  |  |  |  |
| 30 | `PURCHASEINVOICEDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 31 | `PURINVOICEORDPRNCSMSUPTYPE` | CHAR(1) |  |  |  |  |
| 32 | `PURINVOICEORDPRNCSMSUPCODE` | CHAR(8) |  |  |  |  |
| 33 | `PURCHASEINVOICECODE` | CHAR(25) |  |  |  |  |
| 34 | `PURCHASEINVOICEINVOICEDATE` | DATE |  |  |  |  |
| 35 | `POADVPURCHASEORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 36 | `POADVPURCHASEORDERCODE` | CHAR(15) |  |  |  |  |
| 37 | `POADVLINENO` | INTEGER | NOT NULL |  |  |  |
| 38 | `DIRECTINVOICEDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 39 | `DIRECTINVOICECOUNTERCODE` | CHAR(8) |  |  |  |  |
| 40 | `DIRECTINVOICECODE` | CHAR(15) |  |  |  |  |
| 41 | `INVOICENO` | CHAR(25) |  |  |  |  |
| 42 | `INVOICEDATE` | DATE |  |  |  |  |
| 43 | `PLANTINVOICEDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 44 | `PLANTINVOICECODE` | CHAR(15) |  |  |  |  |
| 45 | `EXPINVDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 46 | `EXPINVORDPRNCSMSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 47 | `EXPINVORDPRNCSMSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 48 | `EXPINVCODE` | CHAR(25) |  |  |  |  |
| 49 | `EXPINVINVOICEDATE` | DATE |  |  |  |  |
| 50 | `REFERENCETEXT1` | CHAR(20) |  |  |  |  |
| 51 | `DUEDATE` | DATE |  |  |  |  |
| 52 | `BCDFINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 53 | `BCDFINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 54 | `BCDFINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 55 | `BCDFINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 56 | `BCDFINDOCCODE` | CHAR(15) |  |  |  |  |
| 57 | `CDFINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 58 | `CDFINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 59 | `CDFINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 60 | `CDFINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 61 | `CDFINDOCCODE` | CHAR(15) |  |  |  |  |
| 62 | `FINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 63 | `FINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 64 | `FINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 65 | `FINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 66 | `FINDOCCODE` | CHAR(15) |  |  |  |  |
| 67 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 68 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 69 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 70 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 71 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 72 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 73 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 74 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 75 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 76 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 77 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 78 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 79 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 80 | `INTERUNITCREDITLINE` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFININTERUNITTRNLINE.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.FININTERUNITTRNCOMPANYCODE,
       t.FININTERUNITTRANSACTIONCODE,
       t.LINENO,
       t.ODLBUSINESSUNITCODE,
       t.ODLFINANCIALYEARCODE,
       t.ODLDOCUMENTTEMPLATECODE,
       t.ODLSTATISTICALGROUPCODE,
       t.ODLCODE,
       t.ODLLINENUMBER,
       t.COSTCENTERCODE,
       t.EXCHANGERATE,
       t.AMOUNTTOCLEAR
FROM   DB2ADMIN.LOGFININTERUNITTRNLINE t
FETCH FIRST 100 ROWS ONLY;
```
