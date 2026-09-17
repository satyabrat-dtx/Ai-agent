# DB2ADMIN.ESSEMPLOYEEDOCUMENT

- **Module**: `HR` (low confidence — FK neighbourhood: 1 of 1 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 25
- **Primary key**: `COMPANYCODE`, `EMPLOYEEIDCODE`, `DOCUMENTTYPEICSTABLECODE`, `DOCUMENTTYPECODE`
- **FK degree**: referenced by 0 constraint(s), references 7 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 182782

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `EMPLOYEEIDCODE` | CHAR(9) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `DOCUMENTTYPEICSTABLECODE` | CHAR(4) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `DOCUMENTTYPECODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `DOCUMENTNO` | CHAR(15) |  |  |  |  |
| 5 | `COUNTRYICSTABLECODE` | CHAR(4) |  | FK | foreign_key |  |
| 6 | `COUNTRYCODE` | CHAR(6) |  | FK | foreign_key |  |
| 7 | `STATECODE` | CHAR(3) |  | FK | foreign_key |  |
| 8 | `DISTRICTDISTRICTCODE` | CHAR(3) |  | FK | foreign_key |  |
| 9 | `DOCUMENTISSUEPLACEICSTABLECODE` | CHAR(4) |  | FK | foreign_key |  |
| 10 | `DOCUMENTISSUEPLACECODE` | CHAR(6) |  | FK | foreign_key |  |
| 11 | `DOCUMENTISSUEDATE` | DATE |  |  |  |  |
| 12 | `DOCUMENTEXPIRYDATE` | DATE |  |  |  |  |
| 13 | `DOCUMENTSUBMISSIONDATE` | DATE |  |  |  |  |
| 14 | `REQPENDINGWITH` | CHAR(10) |  |  |  |  |
| 15 | `LINKURL` | VARCHAR(140) |  |  |  |  |
| 16 | `REQUESTFLAG` | INTEGER | NOT NULL |  |  |  |
| 17 | `AUTHLEVEL` | CHAR(10) |  |  |  |  |
| 18 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 19 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 20 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 21 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 22 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 23 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 24 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 7

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `ESSEMPLOYEEDOCUMENT.COMPANYCODE = COMPANY.CODE` |
| `EMPLOYEE_EMPLOYEEID` | `COMPANYCODE`, `EMPLOYEEIDCODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ESSEMPLOYEEDOCUMENT.COMPANYCODE = EMPLOYEE.COMPANYCODE AND ESSEMPLOYEEDOCUMENT.EMPLOYEEIDCODE = EMPLOYEE.CODE` |
| `ICSENTITY_COUNTRY` | `COMPANYCODE`, `COUNTRYICSTABLECODE`, `COUNTRYCODE` | [`ICSENTITY`](../CORE_MASTER/ICSENTITY.md) | `COMPANYCODE`, `ICSTABLECODE`, `CODE` | RESTRICT | `ESSEMPLOYEEDOCUMENT.COMPANYCODE = ICSENTITY.COMPANYCODE AND ESSEMPLOYEEDOCUMENT.COUNTRYICSTABLECODE = ICSENTITY.ICSTABLECODE AND ESSEMPLOYEEDOCUMENT.COUNTRYCODE = ICSENTITY.CODE` |
| `ICSENTITY_DOCUMENTISSUEPLACE` | `COMPANYCODE`, `DOCUMENTISSUEPLACEICSTABLECODE`, `DOCUMENTISSUEPLACECODE` | [`ICSENTITY`](../CORE_MASTER/ICSENTITY.md) | `COMPANYCODE`, `ICSTABLECODE`, `CODE` | RESTRICT | `ESSEMPLOYEEDOCUMENT.COMPANYCODE = ICSENTITY.COMPANYCODE AND ESSEMPLOYEEDOCUMENT.DOCUMENTISSUEPLACEICSTABLECODE = ICSENTITY.ICSTABLECODE AND ESSEMPLOYEEDOCUMENT.DOCUMENTISSUEPLACECODE = ICSENTITY.CODE` |
| `ICSENTITY_DOCUMENTTYPE` | `COMPANYCODE`, `DOCUMENTTYPEICSTABLECODE`, `DOCUMENTTYPECODE` | [`ICSENTITY`](../CORE_MASTER/ICSENTITY.md) | `COMPANYCODE`, `ICSTABLECODE`, `CODE` | RESTRICT | `ESSEMPLOYEEDOCUMENT.COMPANYCODE = ICSENTITY.COMPANYCODE AND ESSEMPLOYEEDOCUMENT.DOCUMENTTYPEICSTABLECODE = ICSENTITY.ICSTABLECODE AND ESSEMPLOYEEDOCUMENT.DOCUMENTTYPECODE = ICSENTITY.CODE` |
| `STATEVSDISTRICT_DISTRICT` | `STATECODE`, `DISTRICTDISTRICTCODE` | [`STATEVSDISTRICT`](../HR/STATEVSDISTRICT.md) | `STATECODE`, `DISTRICTCODE` | RESTRICT | `ESSEMPLOYEEDOCUMENT.STATECODE = STATEVSDISTRICT.STATECODE AND ESSEMPLOYEEDOCUMENT.DISTRICTDISTRICTCODE = STATEVSDISTRICT.DISTRICTCODE` |
| `STATE_STATE` | `STATECODE` | [`STATE`](../HR/STATE.md) | `CODE` | RESTRICT | `ESSEMPLOYEEDOCUMENT.STATECODE = STATE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ESSEMPLOYEEDOCUMENTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.EMPLOYEEIDCODE,
       t.DOCUMENTTYPEICSTABLECODE,
       t.DOCUMENTTYPECODE,
       t.DOCUMENTNO,
       t.COUNTRYICSTABLECODE,
       t.COUNTRYCODE,
       t.STATECODE,
       t.DISTRICTDISTRICTCODE,
       t.DOCUMENTISSUEPLACEICSTABLECODE,
       t.DOCUMENTISSUEPLACECODE,
       t.DOCUMENTISSUEDATE
FROM   DB2ADMIN.ESSEMPLOYEEDOCUMENT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
