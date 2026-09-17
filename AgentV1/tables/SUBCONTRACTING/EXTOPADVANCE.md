# DB2ADMIN.EXTOPADVANCE

- **Module**: `SUBCONTRACTING` (medium confidence — table name starts with 'EXTOP')
- **Roles**: `business_data`
- **Columns**: 38
- **Primary key**: `COMPANYCODE`, `EXTERNALOPERATIONCOUNTERCODE`, `EXTERNALOPERATIONCODE`, `LINENO`
- **FK degree**: referenced by 1 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 221634

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `EXTERNALOPERATIONCOUNTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 2 | `EXTERNALOPERATIONCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 3 | `ADUSGENGROUPTYPECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 4 | `ADUSERGENERICGROUPTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 5 | `ADCODE` | CHAR(10) |  | FK | foreign_key |  |
| 6 | `DUEDATE` | DATE |  |  |  |  |
| 7 | `INVOICEAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 8 | `EXTADVANCEDATE` | DATE | NOT NULL |  |  |  |
| 9 | `PAYMENTADVPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 10 | `PAYMENTADVAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 11 | `CASHDISCOUNTAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 12 | `NETAMTAFTERDEDUCTION` | DECIMAL(18,5) |  |  |  |  |
| 13 | `UPDATEAMTFLAG` | INTEGER | NOT NULL |  |  |  |
| 14 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 15 | `PAYMENTBY` | INTEGER | NOT NULL |  |  |  |
| 16 | `PERCENTAGE` | DECIMAL(5,2) | NOT NULL |  |  |  |
| 17 | `CALCULATEDVALUER` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 18 | `PAYEMENTMADE` | INTEGER | NOT NULL |  |  |  |
| 19 | `POLINE` | CHAR(15) |  |  |  |  |
| 20 | `REMARK2` | DECIMAL(10,0) |  |  |  |  |
| 21 | `REMARK1` | VARCHAR(200) |  |  |  |  |
| 22 | `REMARKS` | CHAR(140) |  |  |  |  |
| 23 | `FLAG` | CHAR(15) |  |  |  |  |
| 24 | `SAPMESSAGE` | LONG VARCHAR |  |  |  |  |
| 25 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 26 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 27 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 28 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 29 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 30 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 31 | `FINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 32 | `FINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 33 | `FINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 34 | `FINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 35 | `FINDOCCODE` | CHAR(15) |  |  |  |  |
| 36 | `OTHFINDOCCODE` | CHAR(15) |  |  |  |  |
| 37 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `EXTOPADVANCE.COMPANYCODE = COMPANY.CODE` |
| `USERGENERICGROUP_AD` | `ADUSGENGROUPTYPECOMPANYCODE`, `ADUSERGENERICGROUPTYPECODE`, `ADCODE` | [`USERGENERICGROUP`](../CORE_MASTER/USERGENERICGROUP.md) | `USERGENGROUPTYPECOMPANYCODE`, `USERGENERICGROUPTYPECODE`, `CODE` | RESTRICT | `EXTOPADVANCE.ADUSGENGROUPTYPECOMPANYCODE = USERGENERICGROUP.USERGENGROUPTYPECOMPANYCODE AND EXTOPADVANCE.ADUSERGENERICGROUPTYPECODE = USERGENERICGROUP.USERGENERICGROUPTYPECODE AND EXTOPADVANCE.ADCODE = USERGENERICGROUP.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `EXTOPADVANCE_LINE` | [`EXTOPADVANCEDETAIL`](../SUBCONTRACTING/EXTOPADVANCEDETAIL.md) | `EXTOPADVANCECOMPANYCODE`, `EXTOPADVANCEEXTOPERATIONCNTCOD`, `EXTOPADVANCEEXTOPERATIONCODE`, `EXTOPADVANCELINENO` | `EXTOPADVANCEDETAIL.EXTOPADVANCECOMPANYCODE = EXTOPADVANCE.COMPANYCODE AND EXTOPADVANCEDETAIL.EXTOPADVANCEEXTOPERATIONCNTCOD = EXTOPADVANCE.EXTERNALOPERATIONCOUNTERCODE AND EXTOPADVANCEDETAIL.EXTOPADVANCEEXTOPERATIONCODE = EXTOPADVANCE.EXTERNALOPERATIONCODE AND EXTOPADVANCEDETAIL.EXTOPADVANCELINENO = EXTOPADVANCE.LINENO` |

## Indexes

- `EXTOPADVANCEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.EXTERNALOPERATIONCOUNTERCODE,
       t.EXTERNALOPERATIONCODE,
       t.ADUSGENGROUPTYPECOMPANYCODE,
       t.ADUSERGENERICGROUPTYPECODE,
       t.ADCODE,
       t.DUEDATE,
       t.INVOICEAMOUNT,
       t.EXTADVANCEDATE,
       t.PAYMENTADVPERCENTAGE,
       t.PAYMENTADVAMOUNT,
       t.CASHDISCOUNTAMOUNT
FROM   DB2ADMIN.EXTOPADVANCE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
