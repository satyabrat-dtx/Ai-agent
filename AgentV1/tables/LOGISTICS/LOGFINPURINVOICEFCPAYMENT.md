# DB2ADMIN.LOGFINPURINVOICEFCPAYMENT

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 32
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 229402

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FINIMPORTFCPAYMENTCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `FINIMPORTFCPAYMENTCODE` | CHAR(5) | NOT NULL |  |  |  |
| 2 | `LINENUMBER` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 3 | `PURINVDIVISIONCODE` | CHAR(3) | NOT NULL |  |  |  |
| 4 | `PURINVORDPRNCSMSUPPLIERTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 5 | `PURINVORDPRNCSMSUPPLIERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 6 | `PURINVCODE` | CHAR(25) | NOT NULL |  |  |  |
| 7 | `PURINVINVOICEDATE` | DATE | NOT NULL |  |  |  |
| 8 | `FINOPENDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 9 | `FINOPENDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 10 | `FINOPENDOCDOCUMENTTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 11 | `FINOPENDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 12 | `FINOPENDOCCODE` | CHAR(15) |  |  |  |  |
| 13 | `FINOPENDOCLINENUMBER` | DECIMAL(7,0) |  |  |  |  |
| 14 | `DOCUMENTCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 15 | `EXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 16 | `DOCUMENTAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 17 | `OUTSTANDINGAMT` | DECIMAL(18,5) |  |  |  |  |
| 18 | `PAYABLEAMT` | DECIMAL(18,5) |  |  |  |  |
| 19 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 20 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 21 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 22 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 23 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 24 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 25 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 26 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 27 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 28 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 29 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 30 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 31 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFINPURINVOICEFCPAYMENT.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.FINIMPORTFCPAYMENTCOMPANYCODE,
       t.FINIMPORTFCPAYMENTCODE,
       t.LINENUMBER,
       t.PURINVDIVISIONCODE,
       t.PURINVORDPRNCSMSUPPLIERTYPE,
       t.PURINVORDPRNCSMSUPPLIERCODE,
       t.PURINVCODE,
       t.PURINVINVOICEDATE,
       t.FINOPENDOCBUSINESSUNITCODE,
       t.FINOPENDOCFINANCIALYEARCODE,
       t.FINOPENDOCDOCUMENTTEMPLATECODE,
       t.FINOPENDOCSTATISTICALGROUPCODE
FROM   DB2ADMIN.LOGFINPURINVOICEFCPAYMENT t
FETCH FIRST 100 ROWS ONLY;
```
